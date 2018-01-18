__author__ = 'Rolando.Morales'


from distutils.core import setup
import py2exe
from py2exe.build_exe import py2exe
import os
import PyQt4.QtCore
import PyQt4.QtGui
import sqlite3



os.environ["PATH"] = \
os.environ["PATH"] + \
os.path.pathsep + os.path.split(PyQt4.__file__)[0]
setup( windows=[{"script": "Contactos.py",
                 "icon_resources": [(1, "d:\contact.ico")]}],
 options={
       "py2exe": {
              "includes":
       ["PyQt4.QtCore", "PyQt4.QtGui","sip","sqlite3" ] } } )
