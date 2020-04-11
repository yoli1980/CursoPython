
import sys
from PyQt5.QtWidgets import QDialog,QApplication,QWidget,QPushButton
from CopiarYPegarDialog import CopiarPegarDialog

class CopiarYPegarDialogAplicacion(QDialog):
    
    def __init__(self):
        super().__init__()
        
        self.ui = CopiarPegarDialog()
        self.ui.setupUi(self)
        
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = CopiarYPegarDialogAplicacion()
    dialogo.show()
    
    sys.exit(app.exec_())
