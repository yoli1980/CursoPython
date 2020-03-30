'''
Created on 30 mar. 2020

@author: Yoli
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ventanas import ventana_principal

def convertir_euros_dolares():
    introducido1 = ui.entrada_euros.text().replace(",",".")
    introducido1_float = float(introducido1)
    dolares = introducido1_float * 1.10
    ui.resultado_dolares.setText("{:.2f}".format(dolares).replace(".",",") + " dólares")
    
def convertir_euros_bolivares():
    introducido2 = ui.entrada_euros.text().replace(",",".")
    introducido2_float = float(introducido2)
    bolivares = introducido2_float * 85891.33
    ui.resultado_bolivares.setText("{:.2f}".format(bolivares).replace(".",",") + " bolivares")

def convertir_euros_libras():
    introducido3 = ui.entrada_euros.text().replace(",",".")
    introducido3_float = float(introducido3)
    libras = introducido3_float * 0.89
    ui.resultado_libras.setText("{:.2f}".format(libras).replace(".",",") + " libras")    

def convertir_euros_yenes():
    introducido4 = ui.entrada_euros.text().replace(",",".")
    introducido4_float = float(introducido4)
    yenes = introducido4_float * 119.17
    ui.resultado_yenes.setText("{:.2f}".format(yenes).replace(".",",") + " yenes")

def convertir_euros_francos():
    introducido5 = ui.entrada_euros.text().replace(",",".")
    introducido5_float = float(introducido5)
    francos = introducido5_float * 1.06
    ui.resultado_francos.setText("{:.2f}".format(francos).replace(".",",") + " francos")


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ventana_principal.Ui_MainWindow()
ui.setupUi(MainWindow)

ui.boton_convertir_dolares.clicked.connect(convertir_euros_dolares)
ui.boton_convertir_yenes.clicked.connect(convertir_euros_yenes)
ui.boton_convertir_francos.clicked.connect(convertir_euros_francos)
ui.boton_convertir_bolivares.clicked.connect(convertir_euros_bolivares)
ui.boton_convertir_libras.clicked.connect(convertir_euros_libras)

MainWindow.show()
sys.exit(app.exec_())