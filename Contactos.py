# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui_contactos2 import Ui_MainWindow
from adicionar_contacto import Adicionar_Contacto
from modificar_contacto import Modificar_Contacto
from enviar_correo import Enivar_Correo
from Conexion import *
from config import *


class Contactos(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(Contactos,self).__init__()
        self.setupUi(self)
       # self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.pushButton.clicked.connect(self.adicionar_contacto)

        self.pushButton_3.clicked.connect(self.eliminar_contacto)
        self.pushButton_2.clicked.connect(self.modificar_contacto)
        self.pushButton_4.clicked.connect(self.configurar_correo)
        self.penviar.clicked.connect(self.send_correo)
        self.plimpiar.clicked.connect(self.limpiar)
        self.pbuscar.clicked.connect(self.buscar_contacto)

        self.conexion=Conexion()
        self.datos_correo=self.conexion.get_correo()
        self.imgTemp=None
        self.l = QVBoxLayout(self.frame_2)
        self.listWidget.itemClicked.connect(self.detallar_contacto)
        self.listWidget.itemDoubleClicked.connect(self.marcar)
        self.nombre.setDisabled(True)
        self.correo.setDisabled(True)
        self.telefono.setDisabled(True)
        self.informacion.setDisabled(True)
        self.contactos=self.conexion.listar_contactos("publico")
        self.listar_contactos()



        self.pushButton.setIcon(QIcon("images/plus.png"))
        self.pushButton_2.setIcon(QIcon("images/update.png"))
        self.pushButton_3.setIcon(QIcon("images/minus.png"))
        self.plimpiar.setIcon(QIcon("images/clear.png"))
        self.pbuscar.setIcon(QIcon("images/search.png"))
        self.penviar.setIcon(QIcon("images/email.png"))
        self.pushButton_4.setIcon(QIcon("images/correo.png"))
        self.setWindowIcon(QIcon("images/contact.png"))

        self.frame_2.setHidden(True)
        self.l.setEnabled(False)
        self.penviar.setDisabled(True)


    def marcar(self,item):
        if  item.checkState()==Qt.Checked:
               item.setCheckState(Qt.Unchecked)
        else:
               item.setCheckState(Qt.Checked)



    def adicionar_contacto(self):
        self.ac=Adicionar_Contacto(self)
        self.ac.show()


    def modificar_contacto(self):
        if self.listWidget.currentRow()!=-1:
           self.mc=Modificar_Contacto(self,self.contactos[self.listWidget.currentRow()])
           self.mc.show()
        else:
             QMessageBox.warning(self,"Error","Debe seleccionar un contacto","")


    def eliminar_contacto(self):
        i_contactos_maracados=[]
        for i in range(0,self.listWidget.count()):
             if self.listWidget.item(i).checkState()==Qt.Checked:
                   i_contactos_maracados.append(i)
        if self.listWidget.currentRow()!=-1 and len(i_contactos_maracados)==0:
               reply = QMessageBox.question(self, 'Confirmar %s'% QApplication.translate("a","Eliminación",None, QApplication.UnicodeUTF8),  QApplication.translate("a","¿Está "
                     "seguro que desea eliminar el contacto seleccionado?",None, QApplication.UnicodeUTF8)
                     ,QMessageBox.Yes |QMessageBox.No, QMessageBox.No)
               if reply == QMessageBox.Yes:
                   try:
                    self.conexion.eliminar_contacto(unicode(self.contactos[self.listWidget.currentRow()][0]),"publico")
                    self.limpiar()
                    QMessageBox.information(self,"Mensaje","Se ha eliminado el contacto","")
                   except:
                    QMessageBox.warning(self,"Mensaje","Ha ocurrido un error al eliminar el contacto seleccionado","")

        elif len(i_contactos_maracados)>0:
           reply = QMessageBox.question(self, 'Confirmar %s'% QApplication.translate("a","Eliminación",None, QApplication.UnicodeUTF8),  QApplication.translate("a","¿Está "
                     "seguro que desea eliminar los contactos seleccionados?",None, QApplication.UnicodeUTF8)
                     ,QMessageBox.Yes |QMessageBox.No, QMessageBox.No)
           if reply == QMessageBox.Yes:
                for item in i_contactos_maracados:
                  self.conexion.eliminar_contacto(self.contactos[item][0],"publico")
                self.limpiar()
                QMessageBox.information(self,"Mensaje","Se han eliminado los contactos","")

        else:
             QMessageBox.warning(self,"Error","Debe seleccionar al menos un contacto","")



    def listar_contactos(self):
       self.penviar.setDisabled(True)
       self.nombre.setText("")
       self.correo.setText("")
       self.telefono.setText("")
       self.informacion.setText("")
       if self.imgTemp!=None:
           self.l.removeWidget(self.imgTemp)
       self.listWidget.clear()
       for i in range(0,len(self.contactos)):
           item=QListWidgetItem(self.contactos[i][1])
           font_item=QFont()
           font_item.setBold(True)
           item.setFont(font_item)
           item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
           item.setCheckState(Qt.Unchecked)
           self.listWidget.addItem(item)




    def detallar_contacto(self,item):
        self.penviar.setDisabled(False)
        self.frame_2.setHidden(False)
        self.l.setEnabled(True)
        if self.imgTemp!=None:
           self.l.removeWidget(self.imgTemp)
        i=int(self.listWidget.currentRow())
        font_informacion=QFont()
        font_telefono=QFont()
        font_correo=QFont()
        font_correo.setPointSize(10)
        font_nombre=QFont()
        font_nombre.setPointSize(10)
        font_informacion.setPointSize(10)
        font_telefono.setPointSize(10)
        self.nombre.setText(self.contactos[i][1])
        self.correo.setText(self.contactos[i][2])
        self.telefono.setText(unicode(self.contactos[i][3]))
        self.informacion.setText(unicode(self.contactos[i][4]))
        self.informacion.setFont(font_informacion)
        self.telefono.setFont(font_telefono)
        self.correo.setFont(font_correo)
        self.nombre.setFont(font_nombre)
        if self.contactos[i][5]!=None:
         qimg = QImage.fromData(self.contactos[i][5])
         pixmap = QPixmap.fromImage(qimg)
         label=QLabel()
         label.setPixmap(pixmap)
         label.setScaledContents(True)
         self.imgTemp=label
         self.l.addWidget(label)
        else:
            self.frame_2.setHidden(True)
            self.l.setEnabled(False)



    def buscar_contacto(self):
        if self.lbuscar.text()!="":
           self.contactos=self.conexion.buscar_contacto(unicode(self.lbuscar.text()),"publico")
           self.lbuscar.setText("")
           self.listWidget.clear()
           for i in range(0,len(self.contactos)):
               item=QListWidgetItem(self.contactos[i][1])
               font_item=QFont()
               font_item.setBold(True)
               item.setFont(font_item)
               item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
               item.setCheckState(Qt.Unchecked)
               self.listWidget.addItem(item)


    def limpiar(self):
         self.item_actual=None
         self.contactos=self.conexion.listar_contactos("publico")
         self.listar_contactos()




    def send_correo(self):
        self.ec=Enivar_Correo(self)
        self.ec.show()


    def configurar_correo(self):
        self.cc=Configurar(self)
        self.cc.show()












if __name__ == '__main__':
        import sys
        app = QApplication(sys.argv)
        app_contactos = Contactos()
        app_contactos.showMaximized()
        sys.exit(app.exec_())









