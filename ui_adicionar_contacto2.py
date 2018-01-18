# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_adicionar_contacto2.ui'
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
        Dialog.resize(499, 373)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.telefono = QtGui.QTextEdit(Dialog)
        self.telefono.setObjectName(_fromUtf8("telefono"))
        self.horizontalLayout_5.addWidget(self.telefono)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.informacion = QtGui.QLabel(Dialog)
        self.informacion.setObjectName(_fromUtf8("informacion"))
        self.horizontalLayout_6.addWidget(self.informacion)
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout_6.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_7.addWidget(self.label_4)
        self.toolButton = QtGui.QToolButton(Dialog)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))



        self.horizontalLayout_7.addWidget(self.toolButton)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.lfoto = QtGui.QLineEdit(Dialog)
        self.lfoto.setObjectName(_fromUtf8("lfoto"))
        self.lay=QtGui.QHBoxLayout()
        self.horizontalLayout_7.addLayout(self.lay)
        self.lay.addWidget(self.toolButton)
        self.lay.addWidget(self.lfoto)
        self.lfoto.setDisabled(True)


        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.horizontalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Adicionar Contacto", None))
        self.label.setText(_translate("Dialog", "Nombre y apellidos", None))
        self.label_2.setText(_translate("Dialog", "Correo..............", None))
        self.label_3.setText(_translate("Dialog", "Teléfonos...........", None))
        self.informacion.setText(_translate("Dialog", "Información extra.", None))
        self.label_4.setText(_translate("Dialog", "Foto..", None))
        self.toolButton.setText(_translate("Dialog", "Foto", None))
        self.pushButton.setText(_translate("Dialog", "Aceptar", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancelar", None))

