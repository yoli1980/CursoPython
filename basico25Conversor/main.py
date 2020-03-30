

from PyQt5 import QtCore, QtGui, QtWidgets
from ventanas import ventana_principal
import sys

#tareas sobre el conversor:
# 1- Crear una aplicacion que permita la conversion de euros a un 
# tipo de moneda a elegir por el programdor
# 2- Añadir 2 botones mas para poder transformar a otros dos tipos 
# de moneda
# 3- Agregar un icono a cada boton representando a cada tipo de moneda

def convertir_de_pesos_a_euros():
    print("Boton pulsado")
    introducido = ui.entrada_pesos.text().replace(",",".")
    introducido_float = float(introducido)
    euros = introducido_float * 0.014
    ui.label_resultado.setText("{:.2f}".format(euros).replace(".",",") + " euros")
    

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = ventana_principal.Ui_MainWindow()
ui.setupUi(MainWindow)

#antes de mostrar ventana principal asigno el codigo a ejecutar cuando
#se haga click en el boton
ui.boton_convertir_a_euros.clicked.connect(convertir_de_pesos_a_euros)


MainWindow.show()
sys.exit(app.exec_())

