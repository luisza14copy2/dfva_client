'''
Created on 21 ago. 2017

@author: luis
'''
import pkcs11
import os
from pkcs11.constants import Attribute
from pkcs11.constants import ObjectClass
import platform
from client_fva import signals
import logging
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.x509.oid import NameOID, ExtensionOID
from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit

logger = logging.getLogger()

class SlotNotFound(Exception):
    pass

class PinNotProvided(Exception):
    pass

class PKCS11Client:
    slot = None
    certificates = None
    key_token = None
    info = None
    settings = None
    keys = None
    identification = None
    slot_number = 0
    cache = {}

    def __init__(self, *args, **kwargs):

        self.settings = kwargs.get('settings', {})
        self.signal = kwargs.get('signal', None)
        self.slot = kwargs.get('slot', None)
        self.session = {}
        self.certificates = {}
        self.keys = {}
        self.lib = None

    def get_slots(self):

        try:
            if self.lib is None:
                self.lib = pkcs11.lib(self.get_module_lib())
            slots = self.lib.get_slots()
        except Exception as e:
            self.signal.send('notify', obj={
                'message': "La biblioteca instalada no funciona para leer las \
                tarjetas, porque no ha instalado las bibliotecas\
                necesarias o porque el sistema operativo no está soportado"
            })
            logger.error("Error abriendo dispositivos PKCS11 %r" % (e,))

        if not slots:
            raise SlotNotFound("PKCS11: Slot not found")

        return slots

    def get_slot(self, slot=None):
        """Obtiene el primer slot (tarjeta) disponible
        .. warning:: Solo usar en pruebas y mejorar la forma como se capta
        """

        if self.slot and slot is None:
            return self.slot
        slots = self.get_slots()
        self.slot = slots[slot or self.slot_number]
        return self.slot

    def get_module_lib(self):
        """Obtiene la biblioteca de comunicación con la tarjeta """

        if hasattr(self.settings, 'module_path') and self.settings.module_path:
            return self.settings.module_path

        if 'PKCS11_MODULE' in os.environ:
            return os.environ['PKCS11_MODULE']

        if os.path.exists('/usr/lib/libASEP11.so'):  # Linux
            return '/usr/lib/libASEP11.so'

        if os.path.exists("/usr/local/lib/libASEP11.dylib"):  # macOS
            return "/usr/local/lib/libASEP11.dylib"

        # FIXME: Hacer la construcción del path por defecto para windows,
        # sugerencia
        """
        public static String ObtenerDirectorioDeWindows()
          {
            String direccionDeWindows = System.getenv("SystemRoot");
            if ((direccionDeWindows == null) || (direccionDeWindows.equalsIgnoreCase(""))) {
              direccionDeWindows = System.getenv("WINDIR");
            }
            String directorioDeWindows = direccionDeWindows + File.separator + "system32";
            return directorioDeWindows;
          }
        """

        _os = platform.system().lower()
        _os_arch = platform.machine()
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if _os == 'linux':
            path = os.path.join(
                BASE_DIR, 'client_fva/libs/%s/%s/libASEP11.so' % (_os, _os_arch))
        elif _os == "darwin":
            path = os.path.join(
                BASE_DIR, 'client_fva/libs/macos/libASEP11.dylib')
        elif _os == "windows":
            path = os.path.join(
                BASE_DIR, 'client_fva/libs/windows/asepkcs.dll')

        if os.path.exists(path):
            return path

        self.signal.send('notify', obj={
            'message': "No existe una biblioteca instalada para leer las \
            tarjetas, esto puede ser porque no ha instalado las bibliotecas \
            necesarias o porque el sistema operativo no está soportado"
        })

    def get_pin(self, pin=None, slot=None):
        """Obtiene el pin de la tarjeta para iniciar sessión"""

        if pin:
            return pin

        if 'PKCS11_PIN' in os.environ:
            pin = os.environ['PKCS11_PIN']
        else:
            try:
                serial = self.get_slot(slot=slot).get_token().serial.decode('utf-8')
            except:
                serial = 'N/D'
                # Fixme: aqui debería manejarse mejor

            sobj = signals.SignalObject(signals.PIN_REQUEST, {'serial': serial})
            respobj = signals.receive(signals.send('pin', sobj))
            pin = respobj.response['pin']
        if pin is None:
            raise PinNotProvided('Sorry PIN is Needed, we will remove this, but for now use export \
            PKCS11_PIN=<pin> before call python')
        return pin
    
    def get_session(self, pin=None, slot=None):
        """Obtiene o inicializa una sessión para el uso de la tarjeta.
        .. warning:: Ojo cachear la session y revisar si está activa
        """

        if slot is None or slot not in self.session:
            slotinst = self.get_slot(slot=slot)
            token = slotinst.get_token()
            session = token.open(user_pin=self.get_pin(pin=pin, slot=slot))
            if slot is not None:
                self.session[slot] = session
            return session
        return self.session[slot]

    def get_certificates(self, slot=None):
        if slot is not None and slot in self.certificates:
            return self.certificates[slot]

        slot_num = slot or 0
        slot = self.get_slot(slot=slot)
        token = slot.get_token()
        self.certificates[slot_num] = {}
        with token.open() as session:
            for cert in session.get_objects({Attribute.CLASS: ObjectClass.CERTIFICATE}):
                cert = x509.load_der_x509_certificate(cert[Attribute.VALUE], default_backend())
                exkey = cert.extensions.get_extension_for_oid(ExtensionOID.EXTENDED_KEY_USAGE)
                is_auth = [exkey.value._usages[x].dotted_string == '1.3.6.1.5.5.7.3.2' for x in range(len(exkey.value._usages))]
                if exkey and any(is_auth):
                    key = 'authentication'
                else:
                    key = 'sign'
                self.certificates[slot_num][key] = cert.public_bytes(serialization.Encoding.PEM)

        return self.certificates[slot_num]

    def get_certificate_info(self, slot=None):

        info = {}
        slot = self.get_slot(slot)
        token = slot.get_token()
        with token.open() as session:
            for cert in session.get_objects({Attribute.CLASS: ObjectClass.CERTIFICATE}):

                cert = x509.load_der_x509_certificate(cert[Attribute.VALUE], default_backend())

                GN = cert.subject.get_attributes_for_oid(NameOID.GIVEN_NAME)[0].value
                SN = cert.subject.get_attributes_for_oid(NameOID.SURNAME)[0].value
                O = cert.subject.get_attributes_for_oid(NameOID.ORGANIZATION_NAME)[0].value
                OU = cert.subject.get_attributes_for_oid(NameOID.ORGANIZATIONAL_UNIT_NAME)[0].value
                C = cert.subject.get_attributes_for_oid(NameOID.COUNTRY_NAME)[0].value

                CN = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value
                name = "%s %s" % (GN,  SN)
                identification = cert.subject.get_attributes_for_oid(NameOID.SERIAL_NUMBER)[0].value
                person = {
                    'name': name.title(),
                    'first_name': GN,
                    'last_name': SN,
                    'identification': identification.replace("CPF-", ''),
                    'type': O,
                    'organization': OU,
                    'country':  C,
                    'commonName': CN,
                    'serialNumber': identification,
                    'cert_serialnumber': str(cert.serial_number),
                    'cert_start': cert.not_valid_before,
                    'cert_expire': cert.not_valid_after
                }
                exkey = cert.extensions.get_extension_for_oid(ExtensionOID.EXTENDED_KEY_USAGE)
                if exkey and any([exkey.value._usages[x].dotted_string == '1.3.6.1.5.5.7.3.2' for x in range(len(exkey.value._usages))]):
                    key = 'authentication'
                else:
                    key = 'sign'

                info[key] = person

        return info

    def get_keys(self, pin=None, slot=None):
        """Extrae los certificados dentro del dispositivo y los guarda de forma
        estructurada para simplificar el acceso"""

        if slot is None or slot not in self.keys:

            keys = {}
            session = self.get_session(pin=pin, slot=slot)
            certs = list(session.get_objects({Attribute.CLASS: ObjectClass.CERTIFICATE}))
            for certificate in certs:
                cert = x509.load_der_x509_certificate(certificate[Attribute.VALUE], default_backend())
                exkey = cert.extensions.get_extension_for_oid(ExtensionOID.EXTENDED_KEY_USAGE)
                if exkey and any([exkey.value._usages[x].dotted_string == '1.3.6.1.5.5.7.3.2' for x in range(len(exkey.value._usages))]):
                    key = 'authentication'
                else:
                    key = 'sign'

                keys[key] = {
                    'pub_key': cert.public_key().public_bytes(
                        serialization.Encoding.PEM, serialization.PublicFormat.PKCS1),
                    'priv_key': list(session.get_objects(
                        {Attribute.CLASS: ObjectClass.PRIVATE_KEY, Attribute.LABEL: certificate[3]}))[0]
                }
            if slot is not None:
                self.keys[slot] = keys
        return self.keys[slot]

    def get_identification(self, slot=None):
        info = None
        try:
            info = self.get_certificate_info(slot=slot)
        except pkcs11.exceptions.TokenNotRecognised as e:
            self.signal.send('notify', obj={
                'message': "No se puede obtener la identificación de la persona, posiblemente porque la tarjeta está mal conectada"
            })
            logger.error("Tarjeta no detectada %r" % (e, ))
        if info:
            self.identification = info['authentication']['identification']
        return self.identification

    def get_tokens_information(self):
        dev = []
        for slot in self.get_slots():
            try:
                token = slot.get_token()
                if token is not None:
                    dev.append({
                                'slot': slot.slot_id,
                                'serial': token.serial.decode(),
                                'label': token.label,
                                'model': token.model,
                                'manufacturer': token.manufacturer_id
                            })
            except pkcs11.exceptions.TokenNotRecognised:
                logger.warning("Token not found %r"%(slot))
        return dev
