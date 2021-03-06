
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from NivelesDialog import NivelesDialog

class NivelesDialogAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        
        self.ui = NivelesDialog()
        self.ui.setupUi(self)
        
        self.ui.hsb_nivel_azucar.valueChanged.connect(self.mostrar_nivel_azucar)
        self.ui.vsb_pulso.valueChanged.connect(self.mostrar_pulso)
        self.ui.hsd_presion_arterial.valueChanged.connect(self.mostrar_presion_arterial)
        self.ui.vsd_nivel_colesterol.valueChanged.connect(self.mostrar_nivel_colesterol)
        
        self.show()
        
    def mostrar_nivel_azucar(self,valor):
        self.ui.txt_resultado.setText("Nivel de azúcar: {}".format(valor))
        
    def mostrar_pulso(self,valor):
        self.ui.txt_resultado.setText("Pulso: {}".format(valor))
    def mostrar_presion_arterial(self,valor):
        self.ui.txt_resultado.setText("Presión arterial: {}".format(valor))
        
    def mostrar_nivel_colesterol(self,valor):
        self.ui.txt_resultado.setText("Nivel de colesterol: {}".format(valor))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = NivelesDialogAplicacion()
    dialogo.show()
    sys.exit(app.exec_())
        