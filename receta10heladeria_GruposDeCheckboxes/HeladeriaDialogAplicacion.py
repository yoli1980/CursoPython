
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QPushButton
from HeladeriaDialog import HeladeriaDialog
from pip._vendor.six import exec_

class HeladeriaDialogAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        
        self.ui = HeladeriaDialog()
        self.ui.setupUi(self)
        
        self.ui.chk_chocolate.stateChanged.connect(self.cacular_total)
        self.ui.chk_vainilla.stateChanged.connect(self.cacular_total)
        self.ui.chk_nata.stateChanged.connect(self.cacular_total)
        self.ui.chk_fresa.stateChanged.connect(self.cacular_total)
        
        self.ui.chk_cafe.stateChanged.connect(self.cacular_total)
        self.ui.chk_agua.stateChanged.connect(self.cacular_total)
        self.ui.chk_cocacola.stateChanged.connect(self.cacular_total)
        
        self.show()
        
    def cacular_total(self):
        precio_inicial = 0
        
        if self.ui.chk_chocolate.isChecked() == True:
            precio_inicial += 3
        if self.ui.chk_vainilla.isChecked() == True:
            precio_inicial += 2
        if self.ui.chk_nata.isChecked() == True:
            precio_inicial += 2
        if self.ui.chk_fresa.isChecked() == True:
            precio_inicial += 2
        
        if self.ui.chk_cafe.isChecked() == True:
            precio_inicial += 2
        if self.ui.chk_agua.isChecked() == True:
            precio_inicial += 1
        if self.ui.chk_cocacola.isChecked() == True:
            precio_inicial += 2
        
        self.ui.lbl_total.setText("Total: {} euros".format(precio_inicial))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = HeladeriaDialogAplicacion()
    dialogo.show()
    sys.exit(app.exec_())