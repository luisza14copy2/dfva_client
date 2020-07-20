# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_fva/ui/ui_elements/signvalidate.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SignValidate(object):
    def setupUi(self, SignValidate):
        SignValidate.setObjectName("SignValidate")
        SignValidate.resize(618, 366)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SignValidate.setWindowIcon(icon)
        SignValidate.setStyleSheet("color:rgb(76, 118, 82);\n"
"background-color:rgb(216, 230, 225);")
        self.signValidateLayout = QtWidgets.QVBoxLayout(SignValidate)
        self.signValidateLayout.setObjectName("signValidateLayout")
        self.titleLabel = QtWidgets.QLabel(SignValidate)
        self.titleLabel.setAcceptDrops(False)
        self.titleLabel.setStyleSheet("font: bold;")
        self.titleLabel.setScaledContents(True)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setWordWrap(True)
        self.titleLabel.setObjectName("titleLabel")
        self.signValidateLayout.addWidget(self.titleLabel)
        self.scrollArea = QtWidgets.QScrollArea(SignValidate)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 592, 290))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetLayout.setObjectName("scrollAreaWidgetLayout")
        self.fileFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.fileFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fileFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fileFrame.setMidLineWidth(0)
        self.fileFrame.setObjectName("fileFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.fileFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_resumen = QtWidgets.QLabel(self.fileFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_resumen.setFont(font)
        self.label_resumen.setStyleSheet("font: bold;\n"
"color: rgb(0, 0, 0);")
        self.label_resumen.setObjectName("label_resumen")
        self.gridLayout.addWidget(self.label_resumen, 0, 2, 1, 1)
        self.label_archivo = QtWidgets.QLabel(self.fileFrame)
        self.label_archivo.setStyleSheet("font: bold;\n"
"color: rgb(0, 0, 0);")
        self.label_archivo.setScaledContents(False)
        self.label_archivo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_archivo.setIndent(0)
        self.label_archivo.setObjectName("label_archivo")
        self.gridLayout.addWidget(self.label_archivo, 0, 0, 1, 1)
        self.resumen = QtWidgets.QTextEdit(self.fileFrame)
        self.resumen.setObjectName("resumen")
        self.gridLayout.addWidget(self.resumen, 3, 2, 3, 1)
        self.razon = QtWidgets.QLineEdit(self.fileFrame)
        self.razon.setObjectName("razon")
        self.gridLayout.addWidget(self.razon, 8, 2, 1, 1)
        self.lugar = QtWidgets.QLineEdit(self.fileFrame)
        self.lugar.setObjectName("lugar")
        self.gridLayout.addWidget(self.lugar, 8, 0, 1, 1)
        self.browseFiles = QtWidgets.QPushButton(self.fileFrame)
        self.browseFiles.setAutoFillBackground(False)
        self.browseFiles.setStyleSheet("color: rgb(11, 35, 21);\n"
"background-color: rgb(229, 229, 229);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browseFiles.setIcon(icon1)
        self.browseFiles.setObjectName("browseFiles")
        self.gridLayout.addWidget(self.browseFiles, 4, 0, 2, 1)
        self.validate = QtWidgets.QPushButton(self.fileFrame)
        self.validate.setEnabled(True)
        self.validate.setSizeIncrement(QtCore.QSize(0, 0))
        self.validate.setBaseSize(QtCore.QSize(0, 0))
        self.validate.setStyleSheet("color: rgb(11, 35, 21);\n"
"background-color: rgb(229, 229, 229);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/validate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.validate.setIcon(icon2)
        self.validate.setIconSize(QtCore.QSize(16, 16))
        self.validate.setObjectName("validate")
        self.gridLayout.addWidget(self.validate, 12, 0, 1, 1)
        self.label_lugar = QtWidgets.QLabel(self.fileFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_lugar.setFont(font)
        self.label_lugar.setStyleSheet("font: bold;\n"
"color: rgb(0, 0, 0);")
        self.label_lugar.setObjectName("label_lugar")
        self.gridLayout.addWidget(self.label_lugar, 7, 0, 1, 1)
        self.filesWidget = SignListAreaWidget(self.fileFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filesWidget.sizePolicy().hasHeightForWidth())
        self.filesWidget.setSizePolicy(sizePolicy)
        self.filesWidget.setAcceptDrops(True)
        self.filesWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.filesWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.filesWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.filesWidget.setAutoScroll(True)
        self.filesWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.filesWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.filesWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.filesWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.filesWidget.setWordWrap(True)
        self.filesWidget.setObjectName("filesWidget")
        self.gridLayout.addWidget(self.filesWidget, 3, 0, 1, 1)
        self.label_razon = QtWidgets.QLabel(self.fileFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_razon.setFont(font)
        self.label_razon.setStyleSheet("font: bold;\n"
"color: rgb(0, 0, 0);")
        self.label_razon.setObjectName("label_razon")
        self.gridLayout.addWidget(self.label_razon, 7, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.sign = QtWidgets.QPushButton(self.fileFrame)
        self.sign.setEnabled(True)
        self.sign.setSizeIncrement(QtCore.QSize(0, 0))
        self.sign.setBaseSize(QtCore.QSize(0, 0))
        self.sign.setStyleSheet("color: rgb(11, 35, 21);\n"
"background-color: rgb(229, 229, 229);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/sign.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sign.setIcon(icon3)
        self.sign.setIconSize(QtCore.QSize(16, 16))
        self.sign.setObjectName("sign")
        self.gridLayout.addWidget(self.sign, 12, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 0, 1, 1)
        self.scrollAreaWidgetLayout.addWidget(self.fileFrame, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.signValidateLayout.addWidget(self.scrollArea)
        self.signValidateProgressBar = QtWidgets.QProgressBar(SignValidate)
        self.signValidateProgressBar.setStyleSheet("")
        self.signValidateProgressBar.setProperty("value", 0)
        self.signValidateProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.signValidateProgressBar.setInvertedAppearance(False)
        self.signValidateProgressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.signValidateProgressBar.setObjectName("signValidateProgressBar")
        self.signValidateLayout.addWidget(self.signValidateProgressBar)

        self.retranslateUi(SignValidate)
        QtCore.QMetaObject.connectSlotsByName(SignValidate)

    def retranslateUi(self, SignValidate):
        _translate = QtCore.QCoreApplication.translate
        SignValidate.setWindowTitle(_translate("SignValidate", "Firmar - Validar Documentos"))
        self.titleLabel.setText(_translate("SignValidate", "Firmar - Validar Documentos"))
        self.label_resumen.setText(_translate("SignValidate", "Resumen"))
        self.label_archivo.setText(_translate("SignValidate", "Archivo"))
        self.browseFiles.setText(_translate("SignValidate", "Archivo"))
        self.validate.setText(_translate("SignValidate", "Validar"))
        self.label_lugar.setToolTip(_translate("SignValidate", "Solo en firmas de documentos PDF"))
        self.label_lugar.setText(_translate("SignValidate", "Lugar*"))
        self.label_razon.setToolTip(_translate("SignValidate", "Solo en firmas de documentos PDF"))
        self.label_razon.setText(_translate("SignValidate", "Razón*"))
        self.sign.setText(_translate("SignValidate", "Firmar"))
        self.signValidateProgressBar.setFormat(_translate("SignValidate", "Sin archivo seleccionado...."))

from client_fva.ui.custom_components.ownsignlistwidget import SignListAreaWidget
from . import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignValidate = QtWidgets.QWidget()
    ui = Ui_SignValidate()
    ui.setupUi(SignValidate)
    SignValidate.show()
    sys.exit(app.exec_())

