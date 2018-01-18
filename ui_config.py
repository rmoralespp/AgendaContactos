# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(424, 194)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ldir = QtGui.QLineEdit(Dialog)
        self.ldir.setText(_fromUtf8(""))
        self.ldir.setObjectName(_fromUtf8("ldir"))
        self.verticalLayout_2.addWidget(self.ldir)
        self.lserver = QtGui.QLineEdit(Dialog)
        self.lserver.setObjectName(_fromUtf8("lserver"))
        self.verticalLayout_2.addWidget(self.lserver)
        self.luser = QtGui.QLineEdit(Dialog)
        self.luser.setObjectName(_fromUtf8("luser"))
        self.verticalLayout_2.addWidget(self.luser)
        self.lpass = QtGui.QLineEdit(Dialog)
        self.lpass.setEchoMode(QtGui.QLineEdit.Password)
        self.lpass.setObjectName(_fromUtf8("lpass"))
        self.verticalLayout_2.addWidget(self.lpass)
        self.lport = QtGui.QLineEdit(Dialog)
        self.lport.setObjectName(_fromUtf8("lport"))
        self.verticalLayout_2.addWidget(self.lport)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.paceptar = QtGui.QPushButton(Dialog)
        self.paceptar.setObjectName(_fromUtf8("paceptar"))
        self.horizontalLayout_2.addWidget(self.paceptar)
        self.pcancelar = QtGui.QPushButton(Dialog)
        self.pcancelar.setObjectName(_fromUtf8("pcancelar"))
        self.horizontalLayout_2.addWidget(self.pcancelar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Configuración de la cuenta de correo", None))
        self.label.setText(_translate("Dialog", "Dirección de correo", None))
        self.label_2.setText(_translate("Dialog", "Servidor de correo saliente (SMTP)", None))
        self.label_3.setText(_translate("Dialog", "Nombre de usuario", None))
        self.label_4.setText(_translate("Dialog", "Contraseña", None))
        self.label_5.setText(_translate("Dialog", "Puerto de Servidor de Salida", None))
        self.paceptar.setText(_translate("Dialog", "Ajustar", None))
        self.pcancelar.setText(_translate("Dialog", "Cancelar", None))

