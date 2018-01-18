#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_config import Ui_Dialog




class Configurar(QDialog,Ui_Dialog):
      def __init__(self,vista_contactos):
        super(Configurar,self).__init__()
        self.setupUi(self)
        self.vista_contactos=vista_contactos
        self.cargar_datos()
        self.pcancelar.clicked.connect(self.hide)
        self.paceptar.clicked.connect(self.configurar_correo)

      def cargar_datos(self):
          if self.vista_contactos.datos_correo!=[]:
              self.ldir.setText(self.vista_contactos.datos_correo[0])
              self.lserver.setText(self.vista_contactos.datos_correo[1])
              self.lport.setText(self.vista_contactos.datos_correo[2])
              self.luser.setText(self.vista_contactos.datos_correo[3])
              self.lpass.setText(self.vista_contactos.datos_correo[4])


      def configurar_correo(self):
          if self.validar()!=False:
              tupla={'dir':unicode(self.ldir.text()),
                     'server':unicode(self.lserver.text()),
                     'port':unicode(self.lport.text()),
                     'usuario':unicode(self.luser.text()),
                     'pass':unicode(self.lpass.text())
                     }
              try:
                self.vista_contactos.conexion.configurar_correo(tupla)
                self.close()
                self.vista_contactos.datos_correo=self.vista_contactos.conexion.get_correo()
                QMessageBox.information(self,"Mensaje","Se ha configurado su cuenta correctamente","")
              except:
                   QMessageBox.warning(self,"Error","Esa cuenta de correo ya existe","")


          else:
              QMessageBox.warning(self,"Error","Compruebe los datos","")



      def validar(self):
          control=True
          if self.ldir.text()=="" or self.lserver.text()=="" or self.lport.text()=="" or self.luser.text()=="" or self.lpass.text()=="":
           control=False
          return control




