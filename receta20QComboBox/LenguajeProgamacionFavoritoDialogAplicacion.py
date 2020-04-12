'''
Created on 12 abr. 2020

@author: Yoli
'''
import sys 
from PyQt5.QtWidgets import QDialog, QApplication
from LenguajesProgramacionDialog import LenguajeProgamacionFavoritoDialog

class LenguajeProgamacionFavoritoDialogAplicacion(QDialog):
    
    def __init__(self):
        super().__init__()
        
        self.ui = LenguajeProgamacionFavoritoDialog()
        self.ui.setupUi(self)
        
        self.ui.cbx_lenguajes.currentIndexChanged.connect(self.seleccionar_lenguaje)
        
        self.show()
        
    def seleccionar_lenguaje(self):
        seleccion = self.ui.cbx_lenguajes.itemText(self.ui.cbx_lenguajes.currentIndex())
        self.ui.lbl_lenguaje_seleccionado.setText("El lenguaje de programación seleccionado es " + seleccion)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = LenguajeProgamacionFavoritoDialogAplicacion()
    dialogo.show()
    
    sys.exit(app.exec_())