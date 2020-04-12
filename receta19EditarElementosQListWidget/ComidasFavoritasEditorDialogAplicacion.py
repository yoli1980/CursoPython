
import sys 
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidget
from ComidasFavoritasEditorDialog import ComidasFavoritasDialog
from PyQt5.Qt import QListWidgetItem

class ComidasFavoritasDialogAplicacion(QDialog):
    
    def __init__(self):
        super().__init__()
        
        self.ui = ComidasFavoritasDialog()
        self.ui.setupUi(self)
        
        #agregamos de forma manual las comidas a la lista
        self.ui.lst_comidas_favoritas.addItem("Pasta")
        self.ui.lst_comidas_favoritas.addItem("Arroz")
        self.ui.lst_comidas_favoritas.addItem("Ensalada")
        self.ui.lst_comidas_favoritas.addItem("Tortilla de patatas")
        
        self.ui.btn_agregrar_comida_favorita.clicked.connect(self.agregar_comida_favorita)
        self.ui.btn_editar_comida_favorita.clicked.connect(self.editar_comida_favorita)
        self.ui.btn_eliminar_comida_favorita.clicked.connect(self.eliminar_comida_favorita)
        self.ui.btn_eliminar_comidas.clicked.connect(self.eliminar_todas_comidas)
        
        self.show()
        
    def agregar_comida_favorita(self):
        self.ui.lst_comidas_favoritas.addItem(self.ui.txt_comida_favorita.text())
        self.ui.txt_comida_favorita.setText("")
        self.ui.txt_comida_favorita.setFocus()
        
    def editar_comida_favorita(self):
        item_seleccionado = self.ui.lst_comidas_favoritas.currentRow() #para recuperar el item a editar
        
        texto, resultado = QInputDialog.getText(self, "Editar comida favorita", "Agregue el nuevo nombre")
        
        if resultado and (len(texto) != 0):
            self.ui.lst_comidas_favoritas.takeItem(self.ui.lst_comidas_favoritas.currentRow())
            self.ui.lst_comidas_favoritas.insertItem(item_seleccionado, QListWidgetItem(texto))
            
    def eliminar_comida_favorita(self):
        self.ui.lst_comidas_favoritas.takeItem(self.ui.lst_comidas_favoritas.currentRow())
    
    def eliminar_todas_comidas(self):
        self.ui.lst_comidas_favoritas.clear()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogo = ComidasFavoritasDialogAplicacion()
    dialogo.show()
    
    sys.exit(app.exec_()) 
        
        