import sys
from client_fva.ui.fvaclientui import Ui_FVAClientUI
from client_fva.ui.myrequests import MyRequests
from client_fva.ui.mysignatures import MySignatures
from client_fva.ui.tab_manager import TabManager
from client_fva.ui.tabdefault import TabDefault
from client_fva.ui.settings import Settings
from client_fva.ui.requestsignature import RequestSignature
from client_fva.ui.requestauthentication import RequestAuthentication
from client_fva.ui.signvalidate import SignValidate
from client_fva.ui.managecontacts import ManageContacts
from client_fva.ui.managecontactgroups import ManageContactGroups
from PyQt5 import QtWidgets, QtGui
from client_fva.user_settings import UserSettings
from client_fva.ui.utils import apply_selected_appearance

main_app = None
fva_client_ui = None
DEFAULT_TAB_INDEX = 0


class FVAClient(Ui_FVAClientUI):

    def __init__(self, main_window):
        Ui_FVAClientUI.__init__(self)
        self.main_window = main_window
        self.setupUi(main_window)
        self.setup_tray_icon()
        self.setup_tab_default_layout()
        self.set_enabled_specific_menu_actions(False)
        self.main_window.closeEvent = self.closeEvent
        self.actionExit.triggered.connect(self.hide)
        self.actionMyRequests.triggered.connect(self.open_my_requests)
        self.actionMySignatures.triggered.connect(self.open_my_signatures)
        self.actionPreferences.triggered.connect(self.open_settings)
        self.actionRequestSignature.triggered.connect(self.open_request_signature)
        self.actionRequestAuthentication.triggered.connect(self.open_request_authentication)
        self.actionSignAuthenticate.triggered.connect(self.open_sign_validate)
        self.actionManageContacts.triggered.connect(self.open_manage_contacts)
        self.actionManageGroups.triggered.connect(self.open_manage_contact_groups)
        self.close_window = False  # by default window is only minimized

        # load initial app settings
        self.user_settings = UserSettings()
        self.user_settings.load()
        apply_selected_appearance(main_app, self.user_settings)

        self.tabmanager=TabManager(self, main_app)

        # TODO - Delete this code because it's for testing
        #my_requests_ui = MyRequests(QtWidgets.QWidget(), main_app)
        #self.usrSlots.insertTab(self.usrSlots.count(), my_requests_ui.widget, "test")
        #self.set_enabled_specific_menu_actions(True)

    def closeEvent(self, event):
        if self.close_window:
            event.accept()
            self.tabmanager.close()
        else:
            event.ignore()
            self.hide()

    def setup_tray_icon(self):
        trayIcon = QtWidgets.QSystemTrayIcon(QtGui.QIcon(":/images/icon.png"), self.main_window)
        menu = QtWidgets.QMenu()
        openAction = menu.addAction("Abrir")
        openAction.triggered.connect(self.show)
        exitAction = menu.addAction("Salir")
        exitAction.triggered.connect(self.exit)
        trayIcon.setContextMenu(menu)
        trayIcon.setToolTip("Cliente FVA")
        trayIcon.activated.connect(self.toggle)
        trayIcon.show()

    def setup_tab_layout(self, new_layout):
        if self.usrSlots.currentIndex() == DEFAULT_TAB_INDEX:
            QtWidgets.QMessageBox.information(self.main_window, 'Seleccione Dispositivo',
                                              "Por favor seleccione una pestaña de dispositivo para acceder a "
                                              "esta opción.")
        else:
            tab = self.usrSlots.currentWidget()
            QtWidgets.QWidget().setLayout(tab.layout())  # cleans current tab layout so a new one can be assigned
            tab.setLayout(new_layout)

    def setup_general_tab_layout(self, new_layout):
        tab = self.tab1
        self.usrSlots.setCurrentIndex(DEFAULT_TAB_INDEX)  # move to general tab
        QtWidgets.QWidget().setLayout(tab.layout())  # cleans current tab layout so a new one can be assigned
        tab.setLayout(new_layout)

    def setup_tab_default_layout(self):
        tab_default = TabDefault(QtWidgets.QWidget(), main_app)
        self.setup_general_tab_layout(tab_default.tabDefaultLayout)

    def show(self):
        self.main_window.show()

    def hide(self):
        self.main_window.hide()

    def exit(self):
        self.close_window = True
        self.tabmanager.close()
        self.main_window.close()

    def toggle(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            if self.main_window.isVisible():
                self.hide()
            else:
                self.show()

    def open_my_requests(self):
        my_requests_ui = MyRequests(QtWidgets.QWidget(), main_app)
        self.setup_tab_layout(my_requests_ui.myRequestsLayout)

    def open_my_signatures(self):
        my_signatures_ui = MySignatures(QtWidgets.QWidget(), main_app)
        self.setup_tab_layout(my_signatures_ui.mySignaturesLayout)

    def open_settings(self):
        settings_ui = Settings(QtWidgets.QWidget(), main_app, fva_client_ui, self.user_settings)
        self.setup_general_tab_layout(settings_ui.settingsLayout)

    def open_request_signature(self):
        request_signature_ui = RequestSignature(QtWidgets.QWidget(), main_app)
        self.setup_tab_layout(request_signature_ui.requestSignatureLayout)

    def open_request_authentication(self):
        request_authentication_ui = RequestAuthentication(QtWidgets.QWidget(), main_app)
        self.setup_tab_layout(request_authentication_ui.requestAuthenticationLayout)

    def open_sign_validate(self):
        sign_validate_ui = SignValidate(QtWidgets.QWidget(), main_app)
        self.setup_tab_layout(sign_validate_ui.signValidateLayout)

    def open_manage_contacts(self):
        manage_contacts_ui = ManageContacts(QtWidgets.QWidget(), main_app)
        self.setup_tab_layout(manage_contacts_ui.manageContactsLayout)

    def open_manage_contact_groups(self):
        manage_contact_groups_ui = ManageContactGroups(QtWidgets.QWidget(), main_app)
        self.setup_tab_layout(manage_contact_groups_ui.manageContactGroupsLayout)

    def set_enabled_specific_menu_actions(self, enabled):
        slot_specific_actions = [self.actionMySignatures, self.actionMyRequests, self.actionRequestSignature,
                                 self.actionRequestAuthentication, self.actionSignAuthenticate,
                                 self.actionManageGroups, self.actionManageContacts]
        for action in slot_specific_actions:
            action.setEnabled(enabled)


def run():
    global main_app
    main_app = QtWidgets.QApplication(sys.argv)
    global fva_client_ui
    fva_client_ui = FVAClient(QtWidgets.QMainWindow())
    fva_client_ui.show()
    sys.exit(main_app.exec_())
