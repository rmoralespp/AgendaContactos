from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_adicionar_contacto2 import Ui_Dialog
import sqlite3
class Modificar_Contacto(QDialog,Ui_Dialog):
      def __init__(self,vista_contactos,contacto):
        super(Modificar_Contacto,self).__init__()
        self.setupUi(self)
        self.vista_contactos=vista_contactos
        self.pushButton.clicked.connect(self.modificar_contacto)
        self.pushButton_2.clicked.connect(self.hide)
        self.toolButton.clicked.connect(self.seleccionar_foto)
        self.ruta_foto=None
        self.contacto=contacto
        self.setWindowTitle("Modificar Contacto")
        self.mostrarContacto()
        self.toolButton.setIcon(QIcon("images/picture.ico"))




      def mostrarContacto(self):
          self.lineEdit.setText(unicode(self.contacto[1]))
          self.lineEdit_2.setText(unicode(self.contacto[2]))
          self.telefono.setText(unicode(self.contacto[3]))
          self.textEdit.setText(unicode(self.contacto[4]))


      def modificar_contacto(self):
         if self.validar()==True:
          contacto={}
          contacto['nombre']=unicode(self.lineEdit.text())
          contacto['correo']=unicode(self.lineEdit_2.text())
          contacto['telefono']=unicode(self.telefono.toPlainText())
          contacto['informacion']=unicode(self.textEdit.toPlainText())
          img=self.readImage()
          if img!=None:
              contacto['foto']=sqlite3.Binary(img)
          else:
              contacto['foto']=self.contacto[5]

          self.vista_contactos.conexion.modificar_contacto(contacto,self.contacto[0],"publico")
          self.close()
          self.vista_contactos.limpiar()
          QMessageBox.information(self,"Mensaje","Se ha modificado el contacto","")


         else:
            QMessageBox.warning(self,"Error","Compruebe los datos","")


      def seleccionar_foto(self):
          self.ruta_foto = QFileDialog.getOpenFileName(self, "Seleciconar foto", "", "(*.jpg *.png)")
          if self.ruta_foto!=None:
            self.lfoto.setText(self.ruta_foto)



      def validar(self):
          control=True
          if self.lineEdit.text()=="":
           control=False
          return control



      def readImage(self):
          try:
              file = open(self.ruta_foto, "rb")
              img = file.read()
              return img
          except:
              return None




