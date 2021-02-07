# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_fva/ui/ui_elements/fvaclient.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FVAClientUI(object):
    def setupUi(self, FVAClientUI):
        FVAClientUI.setObjectName("FVAClientUI")
        FVAClientUI.setEnabled(True)
        FVAClientUI.resize(638, 452)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FVAClientUI.sizePolicy().hasHeightForWidth())
        FVAClientUI.setSizePolicy(sizePolicy)
        FVAClientUI.setMouseTracking(False)
        FVAClientUI.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FVAClientUI.setWindowIcon(icon)
        FVAClientUI.setWindowOpacity(1.0)
        FVAClientUI.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        FVAClientUI.setAnimated(True)
        FVAClientUI.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks)
        FVAClientUI.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(FVAClientUI)
        self.centralWidget.setObjectName("centralWidget")
        self.mainLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.mainLayout.setContentsMargins(11, 11, 11, 11)
        self.mainLayout.setSpacing(6)
        self.mainLayout.setObjectName("mainLayout")
        self.usrSlots = QtWidgets.QTabWidget(self.centralWidget)
        self.usrSlots.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usrSlots.sizePolicy().hasHeightForWidth())
        self.usrSlots.setSizePolicy(sizePolicy)
        self.usrSlots.setAutoFillBackground(False)
        self.usrSlots.setStyleSheet("color:rgb(76, 118, 82);\n"
"background-color:rgb(216, 230, 225);")
        self.usrSlots.setTabPosition(QtWidgets.QTabWidget.North)
        self.usrSlots.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.usrSlots.setElideMode(QtCore.Qt.ElideMiddle)
        self.usrSlots.setUsesScrollButtons(True)
        self.usrSlots.setDocumentMode(False)
        self.usrSlots.setTabsClosable(False)
        self.usrSlots.setMovable(False)
        self.usrSlots.setTabBarAutoHide(False)
        self.usrSlots.setObjectName("usrSlots")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setEnabled(True)
        self.tab1.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tab1.setObjectName("tab1")
        self.tab1Layout = QtWidgets.QGridLayout(self.tab1)
        self.tab1Layout.setContentsMargins(11, 11, 11, 11)
        self.tab1Layout.setSpacing(6)
        self.tab1Layout.setObjectName("tab1Layout")
        self.usrSlots.addTab(self.tab1, "")
        self.mainLayout.addWidget(self.usrSlots)
        FVAClientUI.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(FVAClientUI)
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 638, 22))
        self.menuBar.setAcceptDrops(False)
        self.menuBar.setStyleSheet("QMenu::item{color:rgb(76, 118, 82);\n"
"background-color:rgb(216, 230, 225);}")
        self.menuBar.setNativeMenuBar(False)
        self.menuBar.setObjectName("menuBar")
        self.menuRequests = QtWidgets.QMenu(self.menuBar)
        self.menuRequests.setObjectName("menuRequests")
        self.menuContactos = QtWidgets.QMenu(self.menuBar)
        self.menuContactos.setObjectName("menuContactos")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuFirma = QtWidgets.QMenu(self.menuBar)
        self.menuFirma.setObjectName("menuFirma")
        FVAClientUI.setMenuBar(self.menuBar)
        self.actionRequestSignature = QtWidgets.QAction(FVAClientUI)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRequestSignature.setIcon(icon1)
        self.actionRequestSignature.setStatusTip("")
        self.actionRequestSignature.setWhatsThis("")
        self.actionRequestSignature.setAutoRepeat(True)
        self.actionRequestSignature.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.actionRequestSignature.setIconVisibleInMenu(True)
        self.actionRequestSignature.setObjectName("actionRequestSignature")
        self.actionRequestAuthentication = QtWidgets.QAction(FVAClientUI)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/autentication.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRequestAuthentication.setIcon(icon2)
        self.actionRequestAuthentication.setObjectName("actionRequestAuthentication")
        self.actionManageContacts = QtWidgets.QAction(FVAClientUI)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/manage_contacts.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionManageContacts.setIcon(icon3)
        self.actionManageContacts.setObjectName("actionManageContacts")
        self.actionPreferences = QtWidgets.QAction(FVAClientUI)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/configure_module.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon4)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionMySignatures = QtWidgets.QAction(FVAClientUI)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/my_signatures.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMySignatures.setIcon(icon5)
        self.actionMySignatures.setObjectName("actionMySignatures")
        self.actionMyRequests = QtWidgets.QAction(FVAClientUI)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/my_requests.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMyRequests.setIcon(icon6)
        self.actionMyRequests.setObjectName("actionMyRequests")
        self.actionExit = QtWidgets.QAction(FVAClientUI)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon7)
        self.actionExit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.actionExit.setIconVisibleInMenu(True)
        self.actionExit.setObjectName("actionExit")
        self.actionSignAuthenticate = QtWidgets.QAction(FVAClientUI)
        self.actionSignAuthenticate.setIcon(icon1)
        self.actionSignAuthenticate.setObjectName("actionSignAuthenticate")
        self.actionBitacoras = QtWidgets.QAction(FVAClientUI)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/log.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBitacoras.setIcon(icon8)
        self.actionBitacoras.setObjectName("actionBitacoras")
        self.menuRequests.addAction(self.actionRequestSignature)
        self.menuRequests.addAction(self.actionRequestAuthentication)
        self.menuContactos.addAction(self.actionManageContacts)
        self.menuEdit.addAction(self.actionPreferences)
        self.menuFile.addAction(self.actionMySignatures)
        self.menuFile.addAction(self.actionMyRequests)
        self.menuFile.addAction(self.actionBitacoras)
        self.menuFile.addAction(self.actionExit)
        self.menuFirma.addAction(self.actionSignAuthenticate)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuRequests.menuAction())
        self.menuBar.addAction(self.menuFirma.menuAction())
        self.menuBar.addAction(self.menuContactos.menuAction())

        self.retranslateUi(FVAClientUI)
        self.usrSlots.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FVAClientUI)

    def retranslateUi(self, FVAClientUI):
        _translate = QtCore.QCoreApplication.translate
        FVAClientUI.setWindowTitle(_translate("FVAClientUI", "Cliente FVA"))
        self.usrSlots.setTabText(self.usrSlots.indexOf(self.tab1), _translate("FVAClientUI", "General"))
        self.menuRequests.setTitle(_translate("FVAClientUI", "Solicitar"))
        self.menuContactos.setTitle(_translate("FVAClientUI", "Contactos"))
        self.menuEdit.setTitle(_translate("FVAClientUI", "Editar"))
        self.menuFile.setTitle(_translate("FVAClientUI", "Archivo"))
        self.menuFirma.setTitle(_translate("FVAClientUI", "Mis Documentos"))
        self.actionRequestSignature.setText(_translate("FVAClientUI", "Firma"))
        self.actionRequestSignature.setShortcut(_translate("FVAClientUI", "Ctrl+F"))
        self.actionRequestAuthentication.setText(_translate("FVAClientUI", "Autenticación"))
        self.actionRequestAuthentication.setShortcut(_translate("FVAClientUI", "Ctrl+A"))
        self.actionManageContacts.setText(_translate("FVAClientUI", "Administar Contactos"))
        self.actionManageContacts.setShortcut(_translate("FVAClientUI", "Ctrl+O"))
        self.actionPreferences.setText(_translate("FVAClientUI", "Preferencias"))
        self.actionPreferences.setShortcut(_translate("FVAClientUI", "Ctrl+P"))
        self.actionMySignatures.setText(_translate("FVAClientUI", "Mis Firmas"))
        self.actionMySignatures.setShortcut(_translate("FVAClientUI", "Ctrl+J"))
        self.actionMyRequests.setText(_translate("FVAClientUI", "Mis Solicitudes"))
        self.actionMyRequests.setShortcut(_translate("FVAClientUI", "Ctrl+S"))
        self.actionExit.setText(_translate("FVAClientUI", "Cerrar"))
        self.actionExit.setShortcut(_translate("FVAClientUI", "Ctrl+X"))
        self.actionSignAuthenticate.setText(_translate("FVAClientUI", "Firmar - Validar"))
        self.actionSignAuthenticate.setShortcut(_translate("FVAClientUI", "Ctrl+D"))
        self.actionBitacoras.setText(_translate("FVAClientUI", "Bitácora"))
        self.actionBitacoras.setShortcut(_translate("FVAClientUI", "Ctrl+L"))

from . import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FVAClientUI = QtWidgets.QMainWindow()
    ui = Ui_FVAClientUI()
    ui.setupUi(FVAClientUI)
    FVAClientUI.show()
    sys.exit(app.exec_())

