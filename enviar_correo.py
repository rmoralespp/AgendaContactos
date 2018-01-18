#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_enviar_correo import Ui_MainWindow
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib, os
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate
from email import encoders



class Enivar_Correo(QMainWindow,Ui_MainWindow):
      def __init__(self,vista_contactos):
        super(Enivar_Correo,self).__init__()
        self.setupUi(self)
        self.vista_contactos=vista_contactos
        self.menuEnviar.triggered.connect(self.enviar)
        self.menuCancelar.triggered.connect(self.hide)
        self.menuA_adir_archivo_adjunto.triggered.connect(self.add_archivo_adjunto)
        self.lpara.setText(self.recolectar_destinatarios())
        self.files=[]
        self.layout = QVBoxLayout(self.frame)
        self.files_ck=[]
        self.setWindowIcon(QIcon("images/contact.png"))




      def  enviar(self):
         try:
             #from_address = "rolando.morales@mtss.cu"
             from_address = unicode(self.vista_contactos.datos_correo[0])

             to_address = unicode(self.lpara.text())
             #passw="Correo2015"
             passw=str(self.vista_contactos.datos_correo[4])

             message = unicode(self.textEdit.toPlainText())
             mime_message = MIMEMultipart()
             mime_message["From"] = from_address
             mime_message["To"] = to_address
             mime_message["Subject"] = unicode(self.lasunto.text())
             mime_message["Cc"] = unicode(self.lcc.text())
             destinatarios=to_address.split(";")+mime_message["Cc"].split(";")

             #smtp = SMTP("smtp.mtss.cu",port=25)
             server=unicode(self.vista_contactos.datos_correo[1])
             port=int(unicode(self.vista_contactos.datos_correo[2]))


             smtp = SMTP(server,port=port)
             smtp.login(from_address, passw)
             body = MIMEText(message, "plain", _charset="utf-8")
             mime_message.attach(body)
             self.verificar_listas_chekboxs()
             for f in self.files_ck:
                 f=unicode(f)
                 part = MIMEBase('application', "octet-stream")
                 part.set_payload(open(f,"rb").read())
                 encoders.encode_base64(part)
                 part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
                 mime_message.attach(part)


             smtp.sendmail(from_address,destinatarios , mime_message.as_string())
             smtp.quit()
             QMessageBox.information(self,"Mensaje","El correo se ha enviado correctamente","")
             self.close()
         except:
             QMessageBox.warning(self,"Error","Compruebe los datos, o configure correctamente su cuenta","")



      def add_archivo_adjunto(self):
          self.files = QFileDialog.getOpenFileNames(self, "Seleccionar adjunto/s", "", "(*.*)")
          for file in self.files:
            ck=QCheckBox(self)
            ck.setText(unicode(file))
            ck.setChecked(True)
            self.layout.addWidget(ck)



      def verificar_listas_chekboxs(self):
          for i in range(0,self.layout.count()):
              if self.layout.itemAt(i).widget().checkState()==Qt.Checked:
                  self.files_ck.append(self.layout.itemAt(i).widget().text())




      def recolectar_destinatarios(self):
         destinatarios=""
         for i in range(0,self.vista_contactos.listWidget.count()):
             if self.vista_contactos.listWidget.item(i).checkState()==Qt.Checked:
                if self.vista_contactos.contactos[i][2]!="":
                 destinatarios+=(self.vista_contactos.contactos[i][2]+";")
         if destinatarios=="":
             destinatarios=unicode(self.vista_contactos.correo.text())
         return destinatarios