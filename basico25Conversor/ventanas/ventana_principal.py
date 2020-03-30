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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_introduce_pesos = QtWidgets.QLabel(self.centralwidget)
        self.label_introduce_pesos.setGeometry(QtCore.QRect(10, 130, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_introduce_pesos.setFont(font)
        self.label_introduce_pesos.setObjectName("label_introduce_pesos")
        self.entrada_pesos = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_pesos.setGeometry(QtCore.QRect(250, 140, 141, 31))
        self.entrada_pesos.setObjectName("entrada_pesos")
        self.boton_convertir_a_euros = QtWidgets.QPushButton(self.centralwidget)
        self.boton_convertir_a_euros.setGeometry(QtCore.QRect(160, 200, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.boton_convertir_a_euros.setFont(font)
        self.boton_convertir_a_euros.setObjectName("boton_convertir_a_euros")
        self.label_resultado = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado.setGeometry(QtCore.QRect(100, 290, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_resultado.setFont(font)
        self.label_resultado.setText("")
        self.label_resultado.setObjectName("label_resultado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_introduce_pesos.setText(_translate("MainWindow", "Introduce una cantidad de pesos:"))
        self.boton_convertir_a_euros.setText(_translate("MainWindow", "CONVERTIR A EUROS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
