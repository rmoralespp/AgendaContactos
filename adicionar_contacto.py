
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_adicionar_contacto2 import Ui_Dialog




class Adicionar_Contacto(QDialog,Ui_Dialog):
      def __init__(self,vista_contactos):
        super(Adicionar_Contacto,self).__init__()
        self.setupUi(self)
        self.vista_contactos=vista_contactos
        self.pushButton.clicked.connect(self.adicionar_conatacto)
        self.pushButton_2.clicked.connect(self.hide)
        self.toolButton.clicked.connect(self.seleccionar_foto)
        self.ruta_foto=None
        self.toolButton.setIcon(QIcon("images/picture.ico"))

       



      def adicionar_conatacto(self):
         if self.validar()==True:
          contacto={}
          contacto['nombre']=unicode(self.lineEdit.text())
          contacto['correo']=unicode(self.lineEdit_2.text())
          contacto['telefono']=unicode(self.telefono.toPlainText())
          contacto['informacion']=unicode(self.textEdit.toPlainText())
          contacto['foto']=self.readImage()
          self.vista_contactos.conexion.adicionar_contacto(contacto,"publico")
          self.close()
          self.vista_contactos.limpiar()
          QMessageBox.information(self,"Mensaje","Se ha registrado el contacto correctamente","")

         else:
            QMessageBox.warning(self,"Error","Compruebe los datos","")


      def seleccionar_foto(self):
          self.ruta_foto = QFileDialog.getOpenFileName(self, "Seleciconar foto", "", "(*.jpg *.png)")
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






