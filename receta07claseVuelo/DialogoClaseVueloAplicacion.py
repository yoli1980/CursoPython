

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from DialogoClaseVuelo import DialogoClaseVuelo

class DialogoClaseVueloAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        self.dialogo = DialogoClaseVuelo()
        self.dialogo.setupUi(self)
        
        self.dialogo.rbtn_primera_clase.toggled.connect(self.mostrar_informacion)
        self.dialogo.rbtn_clase_negocios.toggled.connect(self.mostrar_informacion)
        self.dialogo.rbtn_clase_economica.toggled.connect(self.mostrar_informacion)
        
        self.show()
        
    def mostrar_informacion(self):
        coste_vuelo = 0
        
        if self.dialogo.rbtn_primera_clase.isChecked() == True:
            coste_vuelo = 190
        if self.dialogo.rbtn_clase_negocios.isChecked() == True:
            coste_vuelo = 130
        if self.dialogo.rbtn_clase_economica.isChecked() == True:
            coste_vuelo = 99
            
        self.dialogo.lbl_resultado_seleccion.setText("El billete cuesta {} euros".format(coste_vuelo))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = DialogoClaseVueloAplicacion()
    dialogo.show()
    sys.exit(app.exec_())            
            
