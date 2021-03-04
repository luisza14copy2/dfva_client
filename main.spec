# -*- mode: python -*-

block_cipher = None

import platform
_os = platform.system().lower()
_os_arch = platform.machine()

def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )

binaries=[]
if _os == 'linux':
    binaries.append((resource_path('os_libs/%s/%s/libASEP11.so' % (_os, _os_arch)), 
                     'os_libs/%s/%s' % (_os, _os_arch)  ))
if _os == "darwin":
    binaries.append((resource_path('os_libs/macos/libASEP11.dylib'), 'os_libs/macos/'))
if _os == "windows":
    binaries.append( (resource_path('os_libs/windows/asepkcs.dll'), 
                      'os_libs/windows'))


datas = [
(resource_path('certs/ca_bundle.pem'), 'certs'),
(resource_path('LICENSE'), '.')
]


a = Analysis(['main.py'],
             pathex=[resource_path('client_fva/')],
             binaries=binaries,
             datas=datas,
             hiddenimports=['cryptography.hazmat.backends.openssl', 'cffi', 'cryptography.fernet'],
             hookspath=[resource_path('hooks')],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')
if _os == "darwin":
    app = BUNDLE(exe,
             name='dfva_client.app',
             icon=None,
             bundle_identifier=None)
