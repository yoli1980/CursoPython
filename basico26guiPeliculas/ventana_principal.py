# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        MainWindow.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 190, 431, 111))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 26pt \"Comic Sans MS\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 320, 111, 101))
        self.label_2.setStyleSheet("border-image: url(palomitas.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 290, 151, 151))
        self.label_3.setStyleSheet("border-image: url(cine.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        self.menuPel_culas = QtWidgets.QMenu(self.menubar)
        self.menuPel_culas.setObjectName("menuPel_culas")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.submenu_insertar_pelicula = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submenu_insertar_pelicula.setFont(font)
        self.submenu_insertar_pelicula.setObjectName("submenu_insertar_pelicula")
        self.submenu_borrar_pelicula = QtWidgets.QAction(MainWindow)
        self.submenu_borrar_pelicula.setObjectName("submenu_borrar_pelicula")
        self.submenu_listar_peliculas = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submenu_listar_peliculas.setFont(font)
        self.submenu_listar_peliculas.setObjectName("submenu_listar_peliculas")
        self.submenu_inicio = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submenu_inicio.setFont(font)
        self.submenu_inicio.setObjectName("submenu_inicio")
        self.submenu_list_widget_peliculas = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submenu_list_widget_peliculas.setFont(font)
        self.submenu_list_widget_peliculas.setObjectName("submenu_list_widget_peliculas")
        self.submenu_table_widget_peliculas = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.submenu_table_widget_peliculas.setFont(font)
        self.submenu_table_widget_peliculas.setObjectName("submenu_table_widget_peliculas")
        self.menuPel_culas.addAction(self.submenu_insertar_pelicula)
        self.menuPel_culas.addAction(self.submenu_listar_peliculas)
        self.menuPel_culas.addAction(self.submenu_list_widget_peliculas)
        self.menuPel_culas.addAction(self.submenu_table_widget_peliculas)
        self.menuPel_culas.addAction(self.submenu_inicio)
        self.menubar.addAction(self.menuPel_culas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Bienvenid@ a mi aplicación \n"
"de gestión de películas"))
        self.menuPel_culas.setTitle(_translate("MainWindow", "Películas"))
        self.submenu_insertar_pelicula.setText(_translate("MainWindow", "Insertar película"))
        self.submenu_borrar_pelicula.setText(_translate("MainWindow", "Borrar película"))
        self.submenu_listar_peliculas.setText(_translate("MainWindow", "Listar películas"))
        self.submenu_inicio.setText(_translate("MainWindow", "Inicio"))
        self.submenu_list_widget_peliculas.setText(_translate("MainWindow", "Listar películas usando list widget"))
        self.submenu_table_widget_peliculas.setText(_translate("MainWindow", "Listar películas usando table widget"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
