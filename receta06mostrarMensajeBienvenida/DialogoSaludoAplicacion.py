import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from ventana_principal import *


class DialogoSaludoAplicacion(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.dialogo = Ui_DialogoSaludar()
        self.dialogo.setupUi(self)
        
        self.dialogo.btn_saludar.clicked.connect(self.mostrar_saludo)
        self.show()
        
    def mostrar_saludo(self):
        mensaje = self.dialogo.txt_nombre.text()
        self.dialogo.lbl_mensaje_saludo.setText(mensaje)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = DialogoSaludoAplicacion()
    dialogo.show()
    sys.exit(app.exec_())  
    
      
        