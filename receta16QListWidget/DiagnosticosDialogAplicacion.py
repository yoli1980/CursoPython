
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from DiagnosticosDialog import DiagnosticosDialog

class DiagnosticosDialogAplicacion(QDialog):
    
    def __init__(self):
        super().__init__()
        
        self.ui = DiagnosticosDialog()
        self.ui.setupUi(self)
        
        self.ui.lst_diagnosticos.itemClicked.connect(self.seleccion)
        
        self.show()
        
    def seleccion(self):
        self.ui.lbl_resultado.setText("Usted ha seleccionado: \n{}".format(self.ui.lst_diagnosticos.currentItem().text()))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = DiagnosticosDialogAplicacion()
    dialogo.show()
    
    sys.exit(app.exec_())
        
        