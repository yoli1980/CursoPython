

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from DialogoVentaCamisa import DialogoVentaCamisa

class DialogoVentaCamsiaAplicacion(QDialog):
    
    def __init__(self):
        super().__init__()
        self.ui = DialogoVentaCamisa()
        self.ui.setupUi(self)
        
        self.ui.rbtn_xs.toggled.connect(self.mostrar_informacion)
        self.ui.rbtn_s.toggled.connect(self.mostrar_informacion)
        self.ui.rbtn_m.toggled.connect(self.mostrar_informacion)
        self.ui.rbtn_l.toggled.connect(self.mostrar_informacion)
        self.ui.rbtn_xl.toggled.connect(self.mostrar_informacion)
        
        self.ui.rbtn_debito_credito.toggled.connect(self.mostrar_informacion)
        self.ui.rbtn_contrareembolso.toggled.connect(self.mostrar_informacion)
        self.ui.rbtn_transferencia_bancaria.toggled.connect(self.mostrar_informacion)
        
        self.show()
        
    def mostrar_informacion(self):
        talla_seleccionada = ""
        metodo_pago = ""
        
        if self.ui.rbtn_xs.isChecked() == True:
            talla_seleccionada = "XS"
        if self.ui.rbtn_s.isChecked() == True:
            talla_seleccionada = "S"
        if self.ui.rbtn_m.isChecked() == True:
            talla_seleccionada = "M"
        if self.ui.rbtn_l.isChecked() == True:
            talla_seleccionada = "L"
        if self.ui.rbtn_xl.isChecked() == True:
            talla_seleccionada = "XL"    
            
        if self.ui.rbtn_debito_credito.isChecked() == True:
            metodo_pago = "Tarjeta débito/crédito"    
        if self.ui.rbtn_contrareembolso.isChecked() == True:
            metodo_pago = "Contrareembolso"  
        if self.ui.rbtn_transferencia_bancaria.isChecked() == True:
            metodo_pago = "Transferencia bancaria"  
        
        self.ui.lbl_resultado_seleccion.setText("La talla seleccionada es {} \ny el método de pago es {}".format(talla_seleccionada, metodo_pago))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = DialogoVentaCamsiaAplicacion()
    dialogo.show()
    
    sys.exit(app.exec_())
        
        
        