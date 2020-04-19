
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ventana_principal
import ventana_registrar_pelicula
import ventana_listar_peliculas
from modelo.clases import Pelicula
from modelo import operaciones_bd
from PyQt5.Qt import QMessageBox, QPushButton, QFileDialog, QPixmap, QLabel
import ventana_list_widget
import ventana_table_widget
from PyQt5.QtWidgets import QTableWidgetItem
from _functools import partial
import ventana_editar_pelicula
import shutil
import pathlib
from pathlib import Path
from validadores import validadores_pelicula
import ventana_ver_detalles

lista_resultado = None

def registrar_pelicula():
    pelicula = Pelicula()
    
    pelicula.titulo = ui_registrar_pelicula.entrada_titulo_pelicula.text()
    pelicula.titulo = pelicula.titulo.strip()
    resultado_validar_texto = validadores_pelicula.validar_texto(pelicula.titulo)
    if resultado_validar_texto == None:
        ui_registrar_pelicula.lbl_error_titulo.setText("<font color='white'>Título incorrecto</font>")
        return
    else:
        ui_registrar_pelicula.lbl_error_titulo.clear()
    
    pelicula.anio = ui_registrar_pelicula.entrada_anio_pelicula.text()
    resultado_validar_anio = validadores_pelicula.validar_anio(pelicula.anio)
    if resultado_validar_anio == None:
        ui_registrar_pelicula.lbl_error_anio.setText("<font color='white'>Año incorrecto</font>")
        return 
    else:
        ui_registrar_pelicula.lbl_error_anio.clear()
        
    pelicula.duracion = ui_registrar_pelicula.entrada_duracion_pelicula.text()
    resultado_validar_duracion = validadores_pelicula.validar_duracion(pelicula.duracion)
    if resultado_validar_duracion == None:
        ui_registrar_pelicula.lbl_error_duracion.setText("<font color='white'>Duración incorrecta</font>")
        return
    else:
        ui_registrar_pelicula.lbl_error_duracion.clear()
    
    pelicula.pais = ui_registrar_pelicula.entrada_pais_pelicula.text()
    pelicula.pais = pelicula.pais.strip()
    resultado_validar_pais = validadores_pelicula.validar_pais(pelicula.pais)
    if resultado_validar_pais == None:
        ui_registrar_pelicula.lbl_error_pais.setText("<font color='white'>País incorrecto</font>")
        return
    else:
        ui_registrar_pelicula.lbl_error_pais.clear()
            
    pelicula.reparto = ui_registrar_pelicula.entrada_reparto_pelicula.text()
    pelicula.reparto = pelicula.reparto.strip()
    resultado_validar_texto = validadores_pelicula.validar_texto(pelicula.reparto)
    if resultado_validar_texto == None:
        ui_registrar_pelicula.lbl_error_reparto.setText("<font color='white'>Reparto incorrecto</font>")
        return
    else:
        ui_registrar_pelicula.lbl_error_reparto.clear()
        
    pelicula.genero = ui_registrar_pelicula.entrada_genero_pelicula.text()
    pelicula.genero = pelicula.genero.strip()
    resultado_validar_texto = validadores_pelicula.validar_texto(pelicula.genero)
    if resultado_validar_texto == None:
        ui_registrar_pelicula.lbl_error_genero.setText("<font color='white'>Género incorrecto</font>")
        return
    else:
        ui_registrar_pelicula.lbl_error_genero.clear()
    
    pelicula.sinopsis = ui_registrar_pelicula.entrada_sinopsis_pelicula.text()
    pelicula.sinopsis = pelicula.sinopsis.strip()
    resultado_validar_texto = validadores_pelicula.validar_texto(pelicula.sinopsis)
    if resultado_validar_texto == None:
        ui_registrar_pelicula.lbl_error_sinopsis.setText("<font color='white'>Sinópsis incorrecta</font>")
        return
    else:
        ui_registrar_pelicula.lbl_error_sinopsis.clear()
    
    indice_seleccionado = ui_registrar_pelicula.cbx_formato.currentIndex()
    pelicula.formato = ui_registrar_pelicula.cbx_formato.itemText(indice_seleccionado)
    
    if ui_registrar_pelicula.rbtn_mala.isChecked():
        pelicula.valoracion = "Mala"
    if ui_registrar_pelicula.rbtn_regular.isChecked():
        pelicula.valoracion = "Regular"
    if ui_registrar_pelicula.rbtn_buena.isChecked():
        pelicula.valoracion = "Buena"
    if ui_registrar_pelicula.rbtn_muy_buena.isChecked():
        pelicula.valoracion = "Muy buena"
        
    if ui_registrar_pelicula.chbx_vista.isChecked():
        pelicula.vista = True    
    
    id_generado = operaciones_bd.registro_pelicula(pelicula)    
    
    ruta_imagen = "temporal/imagen.jpg"
    objeto_path = Path(ruta_imagen)
    existe = objeto_path.is_file()
    if existe:
        ruta_imagen_destino = "imagenes/" + str(id_generado) + ".jpg"
        shutil.move("temporal/imagen.jpg",ruta_imagen_destino)    
      
    QMessageBox.about(MainWindow,"Info","Registro completado")

def seleccionar_imagen():
    archivo = QFileDialog.getOpenFileName(MainWindow)
    print(archivo)
    ruta_archivo = archivo[0]
    shutil.copy(ruta_archivo,"temporal/imagen.jpg")
    pixmap = QPixmap("temporal/imagen.jpg")
    alto_lbl_imagen = ui_registrar_pelicula.lbl_imagen.height()
    pixmap_redimensianado = pixmap.scaledToHeight(alto_lbl_imagen)    
    ui_registrar_pelicula.lbl_imagen.setPixmap(pixmap_redimensianado)    

def mostrar_registro_peliculas():
    ui_registrar_pelicula.setupUi(MainWindow)
    ui_registrar_pelicula.btn_registrar_pelicula.clicked.connect(registrar_pelicula)
    ui_registrar_pelicula.btn_seleccionar_archivo.clicked.connect(seleccionar_imagen)
    ui_registrar_pelicula.lbl_error_titulo.clear()
    ui_registrar_pelicula.lbl_error_anio.clear()
    ui_registrar_pelicula.lbl_error_duracion.clear()
    ui_registrar_pelicula.lbl_error_pais.clear()
    ui_registrar_pelicula.lbl_error_reparto.clear()
    ui_registrar_pelicula.lbl_error_genero.clear()
    ui_registrar_pelicula.lbl_error_sinopsis.clear()

def mostrar_listado_peliculas():
    ui_listar_peliculas.setupUi(MainWindow)
    lista_resultados = operaciones_bd.obtener_peliculas()
    texto = ""
    for p in lista_resultados:
        texto += "id: " + str(p[0]) + " Título: " + str(p[1]) + " Año: " + str(p[2]) + " Duración: " + str(p[3]) + " País: " + str(p[4]) + " Reparto: " + str(p[5]) + " Género: " + str(p[6]) + " Sinopsis: " + str(p[7]) + " Formato: " + str(p[8]) + " Valoración: " + str(p[9]) + " Vista: " + str(p[10]) + "\n"
    ui_listar_peliculas.listado_libros.setText(texto)    

def mostrar_list_widget():
    global lista_resultado
    ui_list_widget_peliculas.setupUi(MainWindow)
    lista_resultado = operaciones_bd.obtener_peliculas()
    for p in lista_resultado:
        ui_list_widget_peliculas.list_widget_peliculas.addItem("Título: " + str(p[1]) + " Año: " + str(p[2]) + " Duración: " + str(p[3]) + " País: " + str(p[4]) + " Reparto: " + str(p[5]) + " Género: " + str(p[6]) + " Sinopsis: " + str(p[7]) + " Formato: " + str(p[8]) + " Valoración: " + str(p[9]) + " Vista: " + str(p[10]))
    
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
    texto += "Formato: " + lista_resultado[indice_seleccionado][8] + "\n"
    texto += "Valoración: " + lista_resultado[indice_seleccionado][9] + "\n"
    texto += "Vista: " + str(lista_resultado[indice_seleccionado][10]) + "\n"
    QMessageBox.about(MainWindow, "Info", texto)

def mostrar_table_widget():
    ui_table_widget_peliculas.setupUi(MainWindow)
    peliculas = operaciones_bd.obtener_peliculas()
    fila = 0
    for p in peliculas:
        ui_table_widget_peliculas.tabla_peliculas.insertRow(fila)
        columna_indice = 0
        for valor in p:
            if columna_indice == 6:
                if valor == 0:
                    valor = "No"
                else:
                    valor = "Sí"
            
            celda = QTableWidgetItem(str(valor))
            ui_table_widget_peliculas.tabla_peliculas.setItem(fila,columna_indice,celda)
            columna_indice += 1
        
        
        boton_ver_detalles = QPushButton("VER")
        boton_ver_detalles.clicked.connect(partial(ver_detalles,p[0]))
        ui_table_widget_peliculas.tabla_peliculas.setCellWidget(fila,7,boton_ver_detalles)
           
        boton_borrar = QPushButton("BORRAR")
        boton_borrar.clicked.connect(partial(borrar_pelicula,p[0]))
        ui_table_widget_peliculas.tabla_peliculas.setCellWidget(fila,9,boton_borrar)
        
        boton_editar = QPushButton("EDITAR")
        boton_editar.clicked.connect(partial(editar_pelicula,p[0]))
        ui_table_widget_peliculas.tabla_peliculas.setCellWidget(fila,8,boton_editar)
        
        label_miniatura = QLabel()
        ruta_imagen = "imagenes/" + str(p[0]) + ".jpg"
        objeto_path = Path(ruta_imagen)
        existe = objeto_path.is_file()
        if existe == True: 
            pixmap = QPixmap(ruta_imagen)
            pixmap_redimensionado = pixmap.scaledToHeight(40)
            label_miniatura.setPixmap(pixmap_redimensionado)
            ui_table_widget_peliculas.tabla_peliculas.setCellWidget(fila,11,label_miniatura)
        
        fila += 1

def ver_detalles(id):
    QMessageBox.about(MainWindow,"Info","Detalles del registro de id: " + str(id))
    ui_ver_detalles_pelicula.setupUi(MainWindow)
    pelicula = operaciones_bd.obtener_pelicula_por_id(id)
    
    ui_ver_detalles_pelicula.entrada_titulo_pelicula.setText(str(pelicula.titulo))
    ui_ver_detalles_pelicula.entrada_anio_pelicula.setText(str(pelicula.anio))
    ui_ver_detalles_pelicula.entrada_duracion_pelicula.setText(str(pelicula.duracion))
    ui_ver_detalles_pelicula.entrada_pais_pelicula.setText(pelicula.pais)
    ui_ver_detalles_pelicula.entrada_reparto_pelicula.setText(pelicula.reparto)
    ui_ver_detalles_pelicula.entrada_genero_pelicula.setText(pelicula.genero)
    ui_ver_detalles_pelicula.entrada_sinopsis_pelicula.setText(pelicula.sinopsis)
    
    ui_ver_detalles_pelicula.cbx_formato.setCurrentText(pelicula.formato)
    
    if pelicula.valoracion == "Mala":
        ui_ver_detalles_pelicula.rbtn_mala.setChecked(True)
    if pelicula.valoracion == "Regular":
        ui_ver_detalles_pelicula.rbtn_regular.setChecked(True)
    if pelicula.valoracion == "Buena":
        ui_ver_detalles_pelicula.rbtn_buena.setChecked(True)
    if pelicula.valoracion == "Muy buena":
        ui_ver_detalles_pelicula.rbtn_muy_buena.setChecked(True)   
        
    if pelicula.vista:
        ui_ver_detalles_pelicula.chbx_vista.setChecked(True)    
    
    pixmap = QPixmap("imagenes/" + str(pelicula.id) + ".jpg")
    alto_lbl_imagen = ui_ver_detalles_pelicula.lbl_imagen.height()
    pixmap_redimensianado = pixmap.scaledToHeight(alto_lbl_imagen)    
    ui_ver_detalles_pelicula.lbl_imagen.setPixmap(pixmap_redimensianado)
    
def borrar_pelicula(id):
    res = QMessageBox.question(MainWindow,"Info","¿Desea borrar el registro de id: " + str(id) + "?")
    if res == QMessageBox.Yes:
        operaciones_bd.borrar_pelicula(id)
        mostrar_table_widget()

def editar_pelicula(id_a_editar):
    QMessageBox.about(MainWindow,"Info","Vas editar el registro de id: " + str(id_a_editar))
    ui_editar_pelicula.setupUi(MainWindow)
    pelicula_a_editar = operaciones_bd.obtener_pelicula_por_id(id_a_editar)
    ui_editar_pelicula.entrada_titulo_pelicula.setText(str(pelicula_a_editar.titulo))
    ui_editar_pelicula.lbl_error_titulo.clear()
    ui_editar_pelicula.entrada_anio_pelicula.setText(str(pelicula_a_editar.anio))
    ui_editar_pelicula.lbl_error_anio.clear()
    ui_editar_pelicula.entrada_duracion_pelicula.setText(str(pelicula_a_editar.duracion))
    ui_editar_pelicula.lbl_error_duracion.clear()
    ui_editar_pelicula.entrada_pais_pelicula.setText(str(pelicula_a_editar.pais))
    ui_editar_pelicula.lbl_error_pais.clear()
    ui_editar_pelicula.entrada_reparto_pelicula.setText(str(pelicula_a_editar.reparto))
    ui_editar_pelicula.lbl_error_reparto.clear()
    ui_editar_pelicula.entrada_genero_pelicula.setText(str(pelicula_a_editar.genero))
    ui_editar_pelicula.lbl_error_genero.clear()
    ui_editar_pelicula.entrada_sinopsis_pelicula.setText(str(pelicula_a_editar.sinopsis))
    ui_editar_pelicula.lbl_error_sinopsis.clear()
    
    ui_editar_pelicula.cbx_formato.setCurrentText(pelicula_a_editar.formato)
    
    if pelicula_a_editar.valoracion == "Mala":
        ui_editar_pelicula.rbtn_mala.setChecked(True)
    if pelicula_a_editar.valoracion == "Regular":
        ui_editar_pelicula.rbtn_regular.setChecked(True)
    if pelicula_a_editar.valoracion == "Buena":
        ui_editar_pelicula.rbtn_buena.setChecked(True)
    if pelicula_a_editar.valoracion == "Muy buena":
        ui_editar_pelicula.rbtn_muy_buena.setChecked(True)   
        
    if pelicula_a_editar.vista:
        ui_editar_pelicula.chbx_vista.setChecked(True)    
    
    pixmap = QPixmap("imagenes/" + str(pelicula_a_editar.id) + ".jpg")
    alto_lbl_imagen = ui_editar_pelicula.lbl_imagen.height()
    pixmap_redimensianado = pixmap.scaledToHeight(alto_lbl_imagen)    
    ui_editar_pelicula.lbl_imagen.setPixmap(pixmap_redimensianado)
    
    ui_editar_pelicula.btn_seleccionar_archivo.clicked.connect(seleccionar_imagen_editar)
    
    ui_editar_pelicula.btn_guardar_cambios_pelicula.clicked.connect(partial(guardar_cambios_pelicula,pelicula_a_editar.id))
                
def seleccionar_imagen_editar():
    archivo = QFileDialog.getOpenFileName(MainWindow)
    print(archivo)
    ruta_archivo = archivo[0]
    shutil.copy(ruta_archivo,"temporal/imagen.jpg")
    pixmap = QPixmap("temporal/imagen.jpg")
    alto_lbl_imagen = ui_editar_pelicula.lbl_imagen.height()
    pixmap_redimensianado = pixmap.scaledToHeight(alto_lbl_imagen)    
    ui_editar_pelicula.lbl_imagen.setPixmap(pixmap_redimensianado)
    
def guardar_cambios_pelicula(id_a_guardarCambios):
    pelicula_a_guardar_cambios = Pelicula()
    pelicula_a_guardar_cambios.id = id_a_guardarCambios
    pelicula_a_guardar_cambios.titulo = ui_editar_pelicula.entrada_titulo_pelicula.text()
    pelicula_a_guardar_cambios.titulo = pelicula_a_guardar_cambios.titulo.strip()
    resultado_validar_texto = validadores_pelicula.validar_texto(pelicula_a_guardar_cambios.titulo)
    if resultado_validar_texto == None:
        ui_editar_pelicula.lbl_error_titulo.setText("<font color='white'>Título incorrecto</font>")
        return
    else:
        ui_editar_pelicula.lbl_error_titulo.clear()
        
    pelicula_a_guardar_cambios.anio = ui_editar_pelicula.entrada_anio_pelicula.text()
    resultado_validar_anio = validadores_pelicula.validar_anio(pelicula_a_guardar_cambios.anio)
    if resultado_validar_anio == None:
        ui_editar_pelicula.lbl_error_anio.setText("<font color='white'>Año incorrecto</font>")
        return 
    else:
        ui_editar_pelicula.lbl_error_anio.clear()
        
    pelicula_a_guardar_cambios.duracion = ui_editar_pelicula.entrada_duracion_pelicula.text()
    resultado_validar_duracion = validadores_pelicula.validar_duracion(pelicula_a_guardar_cambios.duracion)
    if resultado_validar_duracion == None:
        ui_editar_pelicula.lbl_error_duracion.setText("<font color='white'>Duración incorrecta</font>")
        return
    else:
        ui_editar_pelicula.lbl_error_duracion.clear()    
    
    pelicula_a_guardar_cambios.pais = ui_editar_pelicula.entrada_pais_pelicula.text()
    pelicula_a_guardar_cambios.pais = pelicula_a_guardar_cambios.pais.strip()
    resultado_validar_pais = validadores_pelicula.validar_pais(pelicula_a_guardar_cambios.pais)
    if resultado_validar_pais == None:
        ui_editar_pelicula.lbl_error_pais.setText("<font color='white'>País incorrecto</font>")
        return
    else:
        ui_editar_pelicula.lbl_error_pais.clear()
    
    pelicula_a_guardar_cambios.reparto = ui_editar_pelicula.entrada_reparto_pelicula.text()
    pelicula_a_guardar_cambios.reparto = pelicula_a_guardar_cambios.reparto.strip()
    resultado_validar_texto = validadores_pelicula.validar_texto(pelicula_a_guardar_cambios.reparto)
    if resultado_validar_texto == None:
        ui_editar_pelicula.lbl_error_reparto.setText("<font color='white'>Reparto incorrecto</font>")
        return
    else:
        ui_editar_pelicula.lbl_error_reparto.clear()
    
    pelicula_a_guardar_cambios.genero = ui_editar_pelicula.entrada_genero_pelicula.text()
    pelicula_a_guardar_cambios.genero = pelicula_a_guardar_cambios.genero.strip()
    resultado_validar_texto = validadores_pelicula.validar_texto(pelicula_a_guardar_cambios.genero)
    if resultado_validar_texto == None:
        ui_editar_pelicula.lbl_error_genero.setText("<font color='white'>Género incorrecto</font>")
        return
    else:
        ui_editar_pelicula.lbl_error_genero.clear()
    
    pelicula_a_guardar_cambios.sinopsis = ui_editar_pelicula.entrada_sinopsis_pelicula.text()
    pelicula_a_guardar_cambios.sinopsis = pelicula_a_guardar_cambios.sinopsis.strip()
    resultado_validar_texto = validadores_pelicula.validar_texto(pelicula_a_guardar_cambios.sinopsis)
    if resultado_validar_texto == None:
        ui_editar_pelicula.lbl_error_sinopsis.setText("<font color='white'>Sinópsis incorrecta</font>")
        return
    else:
        ui_editar_pelicula.lbl_error_sinopsis.clear()
      
    pelicula_a_guardar_cambios.formato = ui_editar_pelicula.cbx_formato.currentText()
    
    if ui_editar_pelicula.rbtn_mala.isChecked():
        pelicula_a_guardar_cambios.valoracion = "Mala"
    if ui_editar_pelicula.rbtn_regular.isChecked():
        pelicula_a_guardar_cambios.valoracion = "Regular"
    if ui_editar_pelicula.rbtn_buena.isChecked():
        pelicula_a_guardar_cambios.valoracion = "Buena"
    if ui_editar_pelicula.rbtn_muy_buena.isChecked():
        pelicula_a_guardar_cambios.valoracion = "Muy buena"
        
    if ui_editar_pelicula.chbx_vista.isChecked():
        pelicula_a_guardar_cambios.vista = True    
    
    QMessageBox.about(MainWindow,"Info","Guardando cambios sobre el registro de id: " + str(id_a_guardarCambios))  
    operaciones_bd.guardar_cambios_pelicula(pelicula_a_guardar_cambios)
    
    ruta_imagen = "temporal/imagen.jpg"
    objeto_path = Path(ruta_imagen)
    existe = objeto_path.is_file()
    if existe:
        ruta_imagen_destino = "imagenes/" + str(id_a_guardarCambios) + ".jpg"
        shutil.move("temporal/imagen.jpg",ruta_imagen_destino)
    
    mostrar_table_widget()

def mostrar_inicio():
    ui.setupUi(MainWindow)
    ui.submenu_insertar_pelicula.triggered.connect(mostrar_registro_peliculas)
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
ui_ver_detalles_pelicula = ventana_ver_detalles.Ui_MainWindow()

ui.setupUi(MainWindow)
ui.submenu_insertar_pelicula.triggered.connect(mostrar_registro_peliculas)
ui.submenu_listar_peliculas.triggered.connect(mostrar_listado_peliculas)
ui.submenu_list_widget_peliculas.triggered.connect(mostrar_list_widget)
ui.submenu_table_widget_peliculas.triggered.connect(mostrar_table_widget)
ui.submenu_inicio.triggered.connect(mostrar_inicio)
MainWindow.show()
sys.exit(app.exec_())