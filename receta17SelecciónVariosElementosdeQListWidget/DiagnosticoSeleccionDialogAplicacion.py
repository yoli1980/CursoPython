
import sys 
from PyQt5.QtWidgets import QDialog, QApplication
from DiagnosticosDisponiblesDialog import DiagnosticoSeleccionDialog

class DiagnosticoSeleccionDialogAplicacion(QDialog):
    
    def __init__(self):
        super().__init__()
        
        self.ui = DiagnosticoSeleccionDialog()
        self.ui.setupUi(self)
        
        self.ui.lst_diagnosticos_disponibles.itemSelectionChanged.connect(self.mostrar_seleccion)
        
        self.show()
        
    def mostrar_seleccion(self):
        self.ui.lst_diagnosticos_seleccionados.clear()
        
        diagnosticos = self.ui.lst_diagnosticos_disponibles.selectedItems()
        
        for diagnostico in list(diagnosticos):
            self.ui.lst_diagnosticos_seleccionados.addItem(diagnostico.text())
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = DiagnosticoSeleccionDialogAplicacion()
    dialogo.show()
    
    sys.exit(app.exec_())