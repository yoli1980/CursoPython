

import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from EventosDialog import EventosDialog

class EventosDialogAplicacion(QDialog):
    
    def __init__(self):
        super().__init__()
        
        self.ui = EventosDialog()
        self.ui.setupUi(self)
        
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = EventosDialogAplicacion()
    dialogo.show()
    
    sys.exit(app.exec_())
    