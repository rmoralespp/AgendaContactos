# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enviar_correo.ui'
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
        MainWindow.resize(509, 394)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_4.addWidget(self.frame)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lpara = QtGui.QLineEdit(self.centralwidget)
        self.lpara.setObjectName(_fromUtf8("lpara"))
        self.verticalLayout.addWidget(self.lpara)
        self.lcc = QtGui.QLineEdit(self.centralwidget)
        self.lcc.setObjectName(_fromUtf8("lcc"))
        self.verticalLayout.addWidget(self.lcc)
        self.lasunto = QtGui.QLineEdit(self.centralwidget)
        self.lasunto.setObjectName(_fromUtf8("lasunto"))
        self.verticalLayout.addWidget(self.lasunto)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_3.addWidget(self.textEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuEnviar = QtGui.QAction(self.menubar)
        self.menuEnviar.setObjectName(_fromUtf8("menuEnviar"))
        self.menuCancelar = QtGui.QAction(self.menubar)
        self.menuCancelar.setObjectName(_fromUtf8("menuCancelar"))
        self.menuA_adir_archivo_adjunto = QtGui.QAction(self.menubar)
        self.menuA_adir_archivo_adjunto.setObjectName(_fromUtf8("menuA_adir_archivo_adjunto"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar.addActions([self.menuEnviar,self.menuCancelar,self.menuA_adir_archivo_adjunto])


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Enviar Correo", None))
        self.label_2.setText(_translate("MainWindow", "Para:", None))
        self.label_3.setText(_translate("MainWindow", "CC:", None))
        self.label.setText(_translate("MainWindow", "Asunto:", None))
        self.menuEnviar.setIconText(_translate("MainWindow", "Enviar", None))
        self.menuCancelar.setIconText(_translate("MainWindow", "Cancelar", None))
        self.menuA_adir_archivo_adjunto.setIconText(_translate("MainWindow", "Añadir archivo adjunto", None))

