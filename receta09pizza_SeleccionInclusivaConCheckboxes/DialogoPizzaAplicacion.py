

import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QPushButton
from DialogoPizza import PizzaDialog
from pip._internal.cli.cmdoptions import pre

class PizzaDialogAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        
        self.ui = PizzaDialog()
        self.ui.setupUi(self)
        
        self.ui.chk_queso.stateChanged.connect(self.calcular_precio_final)
        self.ui.chk_aceitunas.stateChanged.connect(self.calcular_precio_final)
        self.ui.chk_salsas.stateChanged.connect(self.calcular_precio_final)
        
        self.show()
        
    def calcular_precio_final(self):
        precio_inicial = 15
        
        if self.ui.chk_queso.isChecked() == True:
            precio_inicial += 1
        if self.ui.chk_aceitunas.isChecked() == True:
            precio_inicial += 1
        if self.ui.chk_salsas.isChecked() == True:
            precio_inicial += 2
            
        self.ui.lbl_precio_final.setText("El precio total es {} euros".format(precio_inicial))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = PizzaDialogAplicacion()
    dialogo.show()
    
    sys.exit(app.exec_())
    
            
        
