# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_ver_detalles.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(478, 601)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(170, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 0, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 20pt \"Comic Sans MS\";")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 200, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 240, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.entrada_titulo_pelicula = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_titulo_pelicula.setEnabled(True)
        self.entrada_titulo_pelicula.setGeometry(QtCore.QRect(150, 49, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.entrada_titulo_pelicula.setFont(font)
        self.entrada_titulo_pelicula.setStyleSheet("color: rgb(255, 255, 255);")
        self.entrada_titulo_pelicula.setReadOnly(True)
        self.entrada_titulo_pelicula.setObjectName("entrada_titulo_pelicula")
        self.entrada_anio_pelicula = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_anio_pelicula.setEnabled(False)
        self.entrada_anio_pelicula.setGeometry(QtCore.QRect(150, 90, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.entrada_anio_pelicula.setFont(font)
        self.entrada_anio_pelicula.setStyleSheet("color: rgb(255, 255, 255);")
        self.entrada_anio_pelicula.setObjectName("entrada_anio_pelicula")
        self.entrada_duracion_pelicula = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_duracion_pelicula.setEnabled(False)
        self.entrada_duracion_pelicula.setGeometry(QtCore.QRect(150, 130, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.entrada_duracion_pelicula.setFont(font)
        self.entrada_duracion_pelicula.setStyleSheet("color: rgb(255, 255, 255);")
        self.entrada_duracion_pelicula.setObjectName("entrada_duracion_pelicula")
        self.entrada_pais_pelicula = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_pais_pelicula.setEnabled(False)
        self.entrada_pais_pelicula.setGeometry(QtCore.QRect(150, 170, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.entrada_pais_pelicula.setFont(font)
        self.entrada_pais_pelicula.setStyleSheet("color: rgb(255, 255, 255);")
        self.entrada_pais_pelicula.setObjectName("entrada_pais_pelicula")
        self.entrada_reparto_pelicula = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_reparto_pelicula.setEnabled(False)
        self.entrada_reparto_pelicula.setGeometry(QtCore.QRect(150, 210, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.entrada_reparto_pelicula.setFont(font)
        self.entrada_reparto_pelicula.setStyleSheet("color: rgb(255, 255, 255);")
        self.entrada_reparto_pelicula.setObjectName("entrada_reparto_pelicula")
        self.entrada_genero_pelicula = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_genero_pelicula.setEnabled(False)
        self.entrada_genero_pelicula.setGeometry(QtCore.QRect(150, 250, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.entrada_genero_pelicula.setFont(font)
        self.entrada_genero_pelicula.setStyleSheet("color: rgb(255, 255, 255);")
        self.entrada_genero_pelicula.setObjectName("entrada_genero_pelicula")
        self.entrada_sinopsis_pelicula = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_sinopsis_pelicula.setEnabled(False)
        self.entrada_sinopsis_pelicula.setGeometry(QtCore.QRect(150, 290, 291, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.entrada_sinopsis_pelicula.setFont(font)
        self.entrada_sinopsis_pelicula.setStyleSheet("color: rgb(255, 255, 255);")
        self.entrada_sinopsis_pelicula.setObjectName("entrada_sinopsis_pelicula")
        self.cbx_formato = QtWidgets.QComboBox(self.centralwidget)
        self.cbx_formato.setEnabled(False)
        self.cbx_formato.setGeometry(QtCore.QRect(150, 330, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        self.cbx_formato.setFont(font)
        self.cbx_formato.setStyleSheet("color: rgb(255, 255, 255);")
        self.cbx_formato.setObjectName("cbx_formato")
        self.cbx_formato.addItem("")
        self.cbx_formato.addItem("")
        self.cbx_formato.addItem("")
        self.cbx_formato.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 280, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 40, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 320, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 360, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 400, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 440, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.lbl_imagen = QtWidgets.QLabel(self.centralwidget)
        self.lbl_imagen.setGeometry(QtCore.QRect(210, 420, 121, 141))
        self.lbl_imagen.setText("")
        self.lbl_imagen.setObjectName("lbl_imagen")
        self.rbtn_mala = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_mala.setEnabled(False)
        self.rbtn_mala.setGeometry(QtCore.QRect(150, 370, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rbtn_mala.setFont(font)
        self.rbtn_mala.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbtn_mala.setObjectName("rbtn_mala")
        self.rbtn_regular = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_regular.setEnabled(False)
        self.rbtn_regular.setGeometry(QtCore.QRect(210, 370, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rbtn_regular.setFont(font)
        self.rbtn_regular.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbtn_regular.setObjectName("rbtn_regular")
        self.rbtn_buena = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_buena.setEnabled(False)
        self.rbtn_buena.setGeometry(QtCore.QRect(290, 370, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rbtn_buena.setFont(font)
        self.rbtn_buena.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbtn_buena.setChecked(True)
        self.rbtn_buena.setObjectName("rbtn_buena")
        self.rbtn_muy_buena = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn_muy_buena.setEnabled(False)
        self.rbtn_muy_buena.setGeometry(QtCore.QRect(360, 370, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rbtn_muy_buena.setFont(font)
        self.rbtn_muy_buena.setStyleSheet("color: rgb(255, 255, 255);")
        self.rbtn_muy_buena.setObjectName("rbtn_muy_buena")
        self.chbx_vista = QtWidgets.QCheckBox(self.centralwidget)
        self.chbx_vista.setEnabled(False)
        self.chbx_vista.setGeometry(QtCore.QRect(150, 410, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chbx_vista.setFont(font)
        self.chbx_vista.setText("")
        self.chbx_vista.setObjectName("chbx_vista")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Detalles de la película:"))
        self.label_3.setText(_translate("MainWindow", "Año:"))
        self.label_4.setText(_translate("MainWindow", "Duración:"))
        self.label_5.setText(_translate("MainWindow", "País:"))
        self.label_6.setText(_translate("MainWindow", "Reparto:"))
        self.label_7.setText(_translate("MainWindow", "Género:"))
        self.cbx_formato.setItemText(0, _translate("MainWindow", "AVI"))
        self.cbx_formato.setItemText(1, _translate("MainWindow", "MP4"))
        self.cbx_formato.setItemText(2, _translate("MainWindow", "MKV"))
        self.cbx_formato.setItemText(3, _translate("MainWindow", "FLV"))
        self.label_8.setText(_translate("MainWindow", "Sinópsis:"))
        self.label_10.setText(_translate("MainWindow", "Título:"))
        self.label_11.setText(_translate("MainWindow", "Formato:"))
        self.label_12.setText(_translate("MainWindow", "Valoración:"))
        self.label_13.setText(_translate("MainWindow", "Vista:"))
        self.label_14.setText(_translate("MainWindow", "Portada:"))
        self.rbtn_mala.setText(_translate("MainWindow", "Mala"))
        self.rbtn_regular.setText(_translate("MainWindow", "Regular"))
        self.rbtn_buena.setText(_translate("MainWindow", "Buena"))
        self.rbtn_muy_buena.setText(_translate("MainWindow", "Muy buena"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
