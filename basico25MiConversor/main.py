'''
Created on 2 abr. 2020

@author: Yoli
'''
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import conversor

def convertir_a_dolares():
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    dolares = introducido_float * 1.09
    ui.lbl_resultado.setText("{:.2f}".format(dolares).replace(".",",") + " \ndólares")

def convertir_a_libras():
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    libras = introducido_float * 0.88
    ui.lbl_resultado.setText("{:.2f}".format(libras).replace(".",",") + " \nlibras")

def convertir_a_francos():
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    francos = introducido_float * 1.06
    ui.lbl_resultado.setText("{:.2f}".format(francos).replace(".",",") + " \nfrancos")    

def convertir_a_yenes():
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    yenes = introducido_float * 117.29
    ui.lbl_resultado.setText("{:.2f}".format(yenes).replace(".",",") + " \nyenes")

def convertir_a_bolivares():
    introducido = ui.entrada_euros.text().replace(",",".")
    introducido_float = float(introducido)
    bolivares = introducido_float * 88389.29
    ui.lbl_resultado.setText("{:.2f}".format(bolivares).replace(".",",") + " \nbolívares")

def resetear():
    ui.entrada_euros.setText("")
    ui.lbl_resultado.setText("")
    
    
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = conversor.Ui_MainWindow()
ui.setupUi(MainWindow)

ui.btn_convertir_dolares.clicked.connect(convertir_a_dolares)
ui.btn_convertir_libras.clicked.connect(convertir_a_libras)
ui.btn_convertir_francos.clicked.connect(convertir_a_francos)
ui.btn_convertir_yenes.clicked.connect(convertir_a_yenes)
ui.btn_convertir_bolivares.clicked.connect(convertir_a_bolivares)
ui.btn_reset.clicked.connect(resetear)

MainWindow.show()
sys.exit(app.exec_())