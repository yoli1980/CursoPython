

import sys 
from PyQt5.QtWidgets import QDialog, QApplication
from ComidasFavoritasDialog import ComidasFavoritasDialog


class ComidasFavoritasDialogAplicacion(QDialog):
    
    def __init__(self):
        super().__init__()
        
        self.ui = ComidasFavoritasDialog()
        self.ui.setupUi(self)
        
        self.ui.btn_agregar_comida.clicked.connect(self.agregar_comida_favorita)
        
        self.show()
        
    def agregar_comida_favorita(self):
        comida_favorita = self.ui.txt_comida_favorita.text()
        
        self.ui.lst_comidas_favoritas.addItem(comida_favorita)
        
        self.ui.txt_comida_favorita.setText("") #para dejar el campo vacio
        self.ui.txt_comida_favorita.setFocus() #para que el cursor se quede ahi
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = ComidasFavoritasDialogAplicacion()
    dialogo.show()
    
    sys.exit(app.exec_())
        