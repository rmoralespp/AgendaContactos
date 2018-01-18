# -*- coding: utf-8 -*-
import sqlite3
import datetime
class Conexion:

     def __init__(self):
        # self.vista_contactos=vista_contactos
         self.ruta=None
         self.conexion=None
         self.cursor=None
         self.connect()
         self.id_usuario=None
        # self.crear_bd()


     def connect(self):
        try:
         self.conexion=sqlite3.connect('contactos.db')
         self.cursor=self.conexion.cursor()
        except:
          self.conexion=None


     def adicionar_contacto(self,contacto,tipo):
         if self.cursor!=None and self.conexion!=None:
          if contacto["foto"]!=None:
           foto=sqlite3.Binary(contacto["foto"])
          else:
            foto=None
          id=unicode(datetime.datetime.now())

          if tipo=="publico":
            query="INSERT INTO Contactos(id,nombre,correo ,telefono,informacion,foto) VALUES (?,?,?,?,?,?)"
            self.cursor.execute(query,(id,contacto["nombre"],contacto["correo"],contacto["telefono"],contacto["informacion"],foto))
            self.conexion.commit()
          elif tipo=="privado":
            query="INSERT INTO Contactos_personales(id,nombre,correo ,telefono,informacion,foto,usuario) VALUES (?,?,?,?,?,?,?)"
            self.cursor.execute(query,(id,contacto["nombre"],contacto["correo"],contacto["telefono"],contacto["informacion"],foto,self.id_usuario))
            self.conexion.commit()





     def listar_contactos(self,tipo):
         if self.cursor!=None:
          if tipo=="publico":
            query="SELECT * from Contactos order by nombre asc"
            self.cursor.execute(query)
            rows=self.cursor.fetchall()
            return rows
          else:
            query="SELECT * from Contactos_personales where usuario=? order by nombre asc"
            self.cursor.execute(query,(self.id_usuario,))
            rows=self.cursor.fetchall()
            return rows
         else:
          return None


     def eliminar_contacto(self,id_contacto,tipo):

          if self.cursor!=None:
              if tipo=="publico":
                query="Delete from Contactos where id=?"
                self.cursor.execute(query,(id_contacto,))
                self.conexion.commit()
              else:
                query="Delete from Contactos_personales where id=? and usuario=?"
                self.cursor.execute(query,(id_contacto,self.id_usuario))
                self.conexion.commit()


     def buscar_contacto(self,nombre,tipo):
        if self.cursor!=None:
          if tipo=="publico":
           query="""SELECT * from Contactos WHERE nombre like ?"""
           self.cursor.execute(query,('%'+nombre+'%',))
           rows=self.cursor.fetchall()
           return rows
          else:
           query="""SELECT * from Contactos_personales WHERE nombre like ? and usuario=?"""
           self.cursor.execute(query,('%'+nombre+'%',self.id_usuario))
           rows=self.cursor.fetchall()
           return rows
        else:
          return []




     def crear_bd(self):
       if self.cursor!=None:
        self.cursor.execute("CREATE TABLE Contactos(id INT PRIMARY KEY, nombre VARCHAR, correo VARCHAR, telefono VARCHAR,informacion VARCHAR, foto BLOB)")



     def modificar_contacto(self,contacto,idv,tipo):
       if self.cursor!=None and self.conexion!=None:
          if tipo=="publico":
            query="UPDATE Contactos set nombre=?,correo=? ,telefono=?,informacion=?,foto=? where id=?"
            self.cursor.execute(query,(contacto["nombre"],contacto["correo"],contacto["telefono"],contacto["informacion"],contacto["foto"],idv))
            self.conexion.commit()

          else:
            query="UPDATE Contactos set nombre=?,correo=? ,telefono=?,informacion=?,foto=? where id=? and usuario=?"
            self.cursor.execute(query,(contacto["nombre"],contacto["correo"],contacto["telefono"],contacto["informacion"],contacto["foto"],idv,self.id_usuario))
            self.conexion.commit()



     def buscar_usuario(self,id,password):
         id=unicode(id)
         password=unicode(password)
         if self.cursor!=None:
            query="""SELECT * from Usuario WHERE id=?"""
            self.cursor.execute(query,(id,))
            rows=self.cursor.fetchall()
            if len(rows)>0:
                if rows[0][3]!=password:
                  return False
                else:
                  return True
            else:
                return False






     def registrar_usuario(self,tupla):
         if self.cursor!=None and self.conexion!=None:
          query="INSERT INTO Usuario(id,nombre,email ,password) VALUES (?,?,?,?)"
          self.cursor.execute(query,(tupla["id"],tupla["nombre"],tupla["email"],tupla["password"]))
          self.conexion.commit()



     def configurar_correo(self,tupla):
        if self.cursor!=None and self.conexion!=None:
          query_delte="Delete from Correo where dir=(SELECT dir from Correo limit 1)"
          self.cursor.execute(query_delte)
          self.conexion.commit()

          query="INSERT INTO Correo(dir,server,port,usuario,pass) VALUES (?,?,?,?,?)"
          self.cursor.execute(query,(tupla["dir"],tupla["server"],tupla["port"],tupla["usuario"],tupla["pass"]))
          self.conexion.commit()


     def get_correo(self):
        if self.cursor!=None and self.conexion!=None:
         query="""SELECT * from Correo"""
         self.cursor.execute(query)
         rows=self.cursor.fetchall()
         if len(rows)>0:
          datos_correo=rows[-1]
          return datos_correo
         else:
             return []
        else:
            return  []

