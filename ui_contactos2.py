# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_contactos2.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(577, 472)
        MainWindow.setMinimumSize(QtCore.QSize(20, 120))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)


        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.plimpiar = QtGui.QPushButton(self.centralwidget)
        self.plimpiar.setObjectName(_fromUtf8("plimpiar"))
        self.horizontalLayout_4.addWidget(self.plimpiar)
        self.pbuscar = QtGui.QPushButton(self.centralwidget)
        self.pbuscar.setObjectName(_fromUtf8("pbuscar"))
        self.horizontalLayout_4.addWidget(self.pbuscar)
        self.lbuscar = QtGui.QLineEdit(self.centralwidget)
        self.lbuscar.setObjectName(_fromUtf8("lbuscar"))
        self.horizontalLayout_4.addWidget(self.lbuscar)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.nombre = QtGui.QLineEdit(self.frame)
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.verticalLayout_2.addWidget(self.nombre)
        self.correo = QtGui.QLineEdit(self.frame)
        self.correo.setObjectName(_fromUtf8("correo"))
        self.verticalLayout_2.addWidget(self.correo)
        self.telefono = QtGui.QTextEdit(self.frame)
        self.telefono.setObjectName(_fromUtf8("telefono"))
        self.verticalLayout_2.addWidget(self.telefono)
        self.informacion = QtGui.QTextEdit(self.frame)
        self.informacion.setObjectName(_fromUtf8("informacion"))
        self.verticalLayout_2.addWidget(self.informacion)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.penviar=QtGui.QPushButton()
        self.penviar.setText("Enviar correo")
        self.verticalLayout_4.addWidget(self.frame_2)
        self.verticalLayout_4.addWidget(self.penviar)
        self.horizontalLayout_3.addWidget(self.frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Contactos", None))
        self.pushButton.setText(_translate("MainWindow", "Adicionar", None))
        self.pushButton_2.setText(_translate("MainWindow", "Modificar", None))
        self.pushButton_3.setText(_translate("MainWindow", "Eliminar", None))
        self.pushButton_4.setText(_translate("MainWindow", "Configurar Correo", None))
        self.plimpiar.setText(_translate("MainWindow", "Limpiar", None))
        self.pbuscar.setText(_translate("MainWindow", "Buscar", None))

