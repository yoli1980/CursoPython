
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ventana_principal
import ventana_registrar_pelicula
import ventana_listar_peliculas
from modelo.clases import Pelicula
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QPushButton
import ventana_list_widget
import ventana_table_widget
from PyQt5.QtWidgets import QTableWidgetItem
from _functools import partial
import ventana_editar_pelicula

lista_resultado = None

def registrar_pelicula():
    pelicula = Pelicula()
    pelicula.titulo = ui_registrar_pelicula.entrada_titulo_pelicula.text()
    pelicula.anio = ui_registrar_pelicula.entrada_anio_pelicula.text()
    pelicula.duracion = ui_registrar_pelicula.entrada_duracion_pelicula.text()
    pelicula.pais = ui_registrar_pelicula.entrada_pais_pelicula.text()
    pelicula.reparto = ui_registrar_pelicula.entrada_reparto_pelicula.text()
    pelicula.genero = ui_registrar_pelicula.entrada_genero_pelicula.text()
    pelicula.sinopsis = ui_registrar_pelicula.entrada_sinopsis_pelicula.text()
    operaciones_bd.registro_pelicula(pelicula)
    QMessageBox.about(MainWindow,"Info","Registro completado")

def mostrar_registo_peliculas():
    ui_registrar_pelicula.setupUi(MainWindow)
    ui_registrar_pelicula.btn_registrar_pelicula.clicked.connect(registrar_pelicula)

def mostrar_listado_peliculas():
    ui_listar_peliculas.setupUi(MainWindow)
    lista_resultados = operaciones_bd.obtener_peliculas()
    texto = ""
    for p in lista_resultados:
        texto += "id: " + str(p[0]) + " Título: " + p[1] + " Año: " + str(p[2]) + " Duración: " + str(p[3]) + " País: " + p[4] + " Reparto: " + p[5] + " Género: " + p[6] + " Sinopsis: " + p[7] + "\n"
    ui_listar_peliculas.listado_libros.setText(texto)    

def mostrar_list_widget():
    global lista_resultado
    ui_list_widget_peliculas.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_peliculas()
    for p in lista_resultado:
        ui_list_widget_peliculas.list_widget_peliculas.addItem("Título: " + p[1] + " Año: " + str(p[2]) + " Duración: " + str(p[3]) + " País: " + p[4] + " Reparto: " + p[5] + " Género: " + p[6] + " Sinopsis: " + p[7])
    
    ui_list_widget_peliculas.list_widget_peliculas.itemClicked.connect(mostrar_registro)
    
def mostrar_registro():
    indice_seleccionado = ui_list_widget_peliculas.list_widget_peliculas.currentRow()
    texto = ""
    texto += "Título: " + lista_resultado[indice_seleccionado][1] + "\n"
    texto += "Año: " + str(lista_resultado[indice_seleccionado][2]) + "\n"
    texto += "Duración: " + str(lista_resultado[indice_seleccionado][3]) + "\n"
    texto += "País: " + lista_resultado[indice_seleccionado][4] + "\n"
    texto += "Reparto: " + lista_resultado[indice_seleccionado][5] + "\n"
    texto += "Género: " + lista_resultado[indice_seleccionado][6] + "\n"
    texto += "Sinopsis: " + lista_resultado[indice_seleccionado][7] + "\n"
    QMessageBox.about(MainWindow, "Info", texto)

def mostrar_table_widget():
    ui_table_widget_peliculas.setupUi(MainWindow)
    peliculas = operaciones_bd.obtener_peliculas()
    fila = 0
    for p in peliculas:
        ui_table_widget_peliculas.tabla_peliculas.insertRow(fila)
        columna_indice = 0
        for valor in p:
            celda = QTableWidgetItem(str(valor))
            ui_table_widget_peliculas.tabla_peliculas.setItem(fila,columna_indice,celda)
            columna_indice += 1
            
        boton_borrar = QPushButton("BORRAR")
        boton_borrar.clicked.connect(partial(borrar_pelicula,p[0]))
        ui_table_widget_peliculas.tabla_peliculas.setCellWidget(fila,9,boton_borrar)
        boton_editar = QPushButton("EDITAR")
        boton_editar.clicked.connect(partial(editar_libro,p[0]))
        ui_table_widget_peliculas.tabla_peliculas.setCellWidget(fila,8,boton_editar)
        fila += 1

def borrar_pelicula(id):
    res = QMessageBox.question(MainWindow,"Info","¿Desea borrar el registro de id: " + str(id) + "?")
    if res == QMessageBox.Yes:
        operaciones_bd.borrar_pelicula(id)
        mostrar_table_widget()

def editar_libro(id_a_editar):
    QMessageBox.about(MainWindow,"Info","Vas editar el registro de id: " + str(id_a_editar))
    ui_editar_pelicula.setupUi(MainWindow)
    pelicula_a_editar = operaciones_bd.obtener_pelicula_por_id(id_a_editar)
    ui_editar_pelicula.entrada_titulo_pelicula.setText(str(pelicula_a_editar.titulo))
    ui_editar_pelicula.entrada_anio_pelicula.setText(str(pelicula_a_editar.anio))
    ui_editar_pelicula.entrada_duracion_pelicula.setText(str(pelicula_a_editar.duracion))
    ui_editar_pelicula.entrada_pais_pelicula.setText(str(pelicula_a_editar.pais))
    ui_editar_pelicula.entrada_reparto_pelicula.setText(str(pelicula_a_editar.reparto))
    ui_editar_pelicula.entrada_genero_pelicula.setText(str(pelicula_a_editar.genero))
    ui_editar_pelicula.entrada_sinopsis_pelicula.setText(str(pelicula_a_editar.sinopsis))
    ui_editar_pelicula.btn_guardar_cambios_pelicula.clicked.connect(partial(guardar_cambios_pelicula,pelicula_a_editar.id))
    
def guardar_cambios_pelicula(id_a_guardarCambios):
    QMessageBox.about(MainWindow,"Info","Guardando cambios sobre el registro de id: " + str(id_a_guardarCambios))
    pelicula_a_guardar_cambios = Pelicula()
    pelicula_a_guardar_cambios.id = id_a_guardarCambios
    pelicula_a_guardar_cambios.titulo = ui_editar_pelicula.entrada_titulo_pelicula.text()
    pelicula_a_guardar_cambios.anio = ui_editar_pelicula.entrada_anio_pelicula.text()
    pelicula_a_guardar_cambios.duracion = ui_editar_pelicula.entrada_duracion_pelicula.text()
    pelicula_a_guardar_cambios.pais = ui_editar_pelicula.entrada_pais_pelicula.text()
    pelicula_a_guardar_cambios.reparto = ui_editar_pelicula.entrada_reparto_pelicula.text()
    pelicula_a_guardar_cambios.genero = ui_editar_pelicula.entrada_genero_pelicula.text()
    pelicula_a_guardar_cambios.sinopsis =ui_editar_pelicula.entrada_sinopsis_pelicula.text()
    operaciones_bd.guardar_cambios_pelicula(pelicula_a_guardar_cambios)
    mostrar_table_widget()

def mostrar_inicio():
    ui.setupUi(MainWindow)
    ui.submenu_insertar_pelicula.triggered.connect(mostrar_registo_peliculas)
    ui.submenu_listar_peliculas.triggered.connect(mostrar_listado_peliculas)
    ui.submenu_list_widget_peliculas.triggered.connect(mostrar_list_widget)
    ui.submenu_table_widget_peliculas.triggered.connect(mostrar_table_widget)
    ui.submenu_inicio.triggered.connect(mostrar_inicio)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ventana_principal.Ui_MainWindow()
ui_registrar_pelicula = ventana_registrar_pelicula.Ui_MainWindow()
ui_listar_peliculas = ventana_listar_peliculas.Ui_MainWindow()
ui_list_widget_peliculas = ventana_list_widget.Ui_MainWindow()
ui_table_widget_peliculas = ventana_table_widget.Ui_MainWindow()
ui_editar_pelicula = ventana_editar_pelicula.Ui_MainWindow()

ui.setupUi(MainWindow)
ui.submenu_insertar_pelicula.triggered.connect(mostrar_registo_peliculas)
ui.submenu_listar_peliculas.triggered.connect(mostrar_listado_peliculas)
ui.submenu_list_widget_peliculas.triggered.connect(mostrar_list_widget)
ui.submenu_table_widget_peliculas.triggered.connect(mostrar_table_widget)
ui.submenu_inicio.triggered.connect(mostrar_inicio)
MainWindow.show()
sys.exit(app.exec_())