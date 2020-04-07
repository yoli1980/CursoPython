'''
Created on 31 mar. 2020

@author: Yoli
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ventanas import ventana_principal, ventana_registrar_libro,\
    ventana_listado_libros, ventana_list_widget, ventana_table_widget
from modelo.clases import Libro
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QTableWidgetItem

#variable con el resultado de base de datos
lista_resultado = None

def registrar_libro():
    libro = Libro()
    libro.titulo = ui_registrar_libro.entrada_titulol_libro.text()
    libro.paginas = ui_registrar_libro.entrada_paginas_libro.text()
    libro.precio = ui_registrar_libro.entrada_precio_libro.text()
    operaciones_bd.registro_libro(libro)
    QMessageBox.about(MainWindow,"Info","¡Tu libro queda registrado!")    
def mostar_registro_libro():
    ui_registrar_libro.setupUi(MainWindow)
    ui_registrar_libro.boton_registrar_libro.clicked.connect(registrar_libro)
def mostrar_listado_libros():
    ui_listar_libros.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_libros()
    texto = ""
    for l in lista_resultado:
        texto += "id: " + str(l[0]) + " titulo: " + l[1] + " páginas: " + str(l[2]) + " precio: " + str(l[3]) + "\n"
    ui_listar_libros.listado_libros.setText(texto)

def mostrar_list_widget():
    global lista_resultado
    ui_ventana_list_widget.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_libros()
    #voy a rellenar el list widget
    for l in lista_resultado:
        ui_ventana_list_widget.list_widget_libros.addItem("Título: " + l[1] + " Páginas: " + str(l[2]) + " Precio: " + str(l[3]))
        
    ui_ventana_list_widget.list_widget_libros.itemClicked.connect(mostrar_registro)

#funcion  que muestra toda la informacion cuando se haga click 
#en un elemento del list widget    
def mostrar_registro():
    indice_seleccionado = ui_ventana_list_widget.list_widget_libros.currentRow()
    texto = ""
    texto += "Título: " + lista_resultado[indice_seleccionado][1] + "\n"
    texto += "Páginas: " + str(lista_resultado[indice_seleccionado][2]) + "\n"
    texto += "Precio: " + str(lista_resultado[indice_seleccionado][3])
    QMessageBox.about(MainWindow, "Info", texto)

def mostrar_table_widget():
    ui_ventana_table_widget.setupUi(MainWindow)
    #vamos a rellenar la tabla
    libros = operaciones_bd.obtener_libros()
    fila = 0
    for l in libros:
        ui_ventana_table_widget.tabla_libros.insertRow(fila) #creo la fila
        #celda para el id
        celda = QTableWidgetItem(str(l[0])) #creo la celda
        ui_ventana_table_widget.tabla_libros.setItem(fila,0,celda)
        #celda para el nombre
        celda = QTableWidgetItem(str(l[1]))
        ui_ventana_table_widget.tabla_libros.setItem(fila,1,celda)
        #celda para las paginas
        celda = QTableWidgetItem(str(l[2]))
        ui_ventana_table_widget.tabla_libros.setItem(fila,2,celda)
        #celda para el precio
        celda = QTableWidgetItem(str(l[3]))
        ui_ventana_table_widget.tabla_libros.setItem(fila,3,celda)
        
        fila += 1
        
def mostrar_inicio():
    ui.setupUi(MainWindow)

#inicio aplicacion principal:
app = QtWidgets.QApplication(sys.argv) #linea obligatoria para usar pyqt5
MainWindow = QtWidgets.QMainWindow() #crea una ventana principal con pyqt5
ui = ventana_principal.Ui_MainWindow() #creo el interfaz definido por ventana_principal.py
#que es el archivo generado desde la consola a partir
#del archivo de diseño ventana_principal.ui
ui_registrar_libro = ventana_registrar_libro.Ui_MainWindow() #lo mismo pero para registrar libro
ui_listar_libros = ventana_listado_libros.Ui_MainWindow()#lo mismo pero para listar libros
ui_ventana_list_widget = ventana_list_widget.Ui_MainWindow()
ui_ventana_table_widget = ventana_table_widget.Ui_MainWindow()
ui.setupUi(MainWindow)#todo lo que tiene el interfaz de la ventana principal lo pongo en el MainWindow

ui.submenu_insertar_libro.triggered.connect(mostar_registro_libro)
ui.submenu_listar_libros.triggered.connect(mostrar_listado_libros)
ui.submenu_list_widget_libros.triggered.connect(mostrar_list_widget)
ui.submenu_table_widget_libros.triggered.connect(mostrar_table_widget)
ui.submenu_inicio.triggered.connect(mostrar_inicio)
    
                      
MainWindow.show()#mostrar la ventana principal de pyqt5
sys.exit(app.exec_())#cerrar la aplicacion cuando se cierra la ventana MainWindow