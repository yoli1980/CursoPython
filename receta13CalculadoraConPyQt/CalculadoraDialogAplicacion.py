
import sys
from PyQt5.QtWidgets import QDialog,QApplication,QWidget,QPushButton
from CalculadoraDialog import CalculadoraDialog

class CalculadoraDialogAplicacion(QDialog):
    
    def __init__(self):
        super().__init__()
        
        self.ui = CalculadoraDialog()
        self.ui.setupUi(self)
        
        self.ui.btn_sumar.clicked.connect(self.sumar)
        self.ui.btn_restar.clicked.connect(self.restar)
        self.ui.btn_multiplicar.clicked.connect(self.multiplicar)
        self.ui.btn_dividir.clicked.connect(self.dividir)
        
        self.show()
        
    def sumar(self):
        suma = 0
        operando1 = 0
        operando2 = 0
        if len(self.ui.txt_primer_numero.text()) > 0 :
            operando1 = int(self.ui.txt_primer_numero.text());
        if len(self.ui.txt_segundo_numero.text()) > 0 :
            operando2 = int(self.ui.txt_segundo_numero.text())
        
        suma = operando1 + operando2
        
        self.ui.lbl_resultado.setText(str(suma))
        
    def restar(self):
        resta = 0
        operando1 = 0
        operando2 = 0
        if len(self.ui.txt_primer_numero.text()) > 0 :
            operando1 = int(self.ui.txt_primer_numero.text());
        if len(self.ui.txt_segundo_numero.text()) > 0 :
            operando2 = int(self.ui.txt_segundo_numero.text())
        
        resta = operando1 - operando2
        
        self.ui.lbl_resultado.setText(str(resta))
        
    def multiplicar(self):
        multiplicacion = 0
        operando1 = 0
        operando2 = 0
        if len(self.ui.txt_primer_numero.text()) > 0 :
            operando1 = int(self.ui.txt_primer_numero.text());
        if len(self.ui.txt_segundo_numero.text()) > 0 :
            operando2 = int(self.ui.txt_segundo_numero.text())
        
        multiplicacion = operando1 * operando2
        
        self.ui.lbl_resultado.setText(str(multiplicacion))
        
    def dividir(self):
        division = 0
        operando1 = 0
        operando2 = 0
        if len(self.ui.txt_primer_numero.text()) > 0 :
            operando1 = int(self.ui.txt_primer_numero.text());
        if len(self.ui.txt_segundo_numero.text()) > 0 :
            operando2 = int(self.ui.txt_segundo_numero.text())
        
        division = operando1 / operando2
        
        self.ui.lbl_resultado.setText(str(division))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = CalculadoraDialogAplicacion()
    dialogo.show()
    
    sys.exit(app.exec_())
        
        