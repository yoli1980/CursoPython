# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'conversor.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 70, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.entrada_euros = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_euros.setGeometry(QtCore.QRect(170, 130, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.entrada_euros.setFont(font)
        self.entrada_euros.setObjectName("entrada_euros")
        self.lbl_resultado = QtWidgets.QLabel(self.centralwidget)
        self.lbl_resultado.setGeometry(QtCore.QRect(170, 340, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_resultado.setFont(font)
        self.lbl_resultado.setText("")
        self.lbl_resultado.setObjectName("lbl_resultado")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_convertir_dolares = QtWidgets.QPushButton(self.centralwidget)
        self.btn_convertir_dolares.setGeometry(QtCore.QRect(50, 290, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_convertir_dolares.setFont(font)
        self.btn_convertir_dolares.setObjectName("btn_convertir_dolares")
        self.btn_convertir_libras = QtWidgets.QPushButton(self.centralwidget)
        self.btn_convertir_libras.setGeometry(QtCore.QRect(130, 290, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_convertir_libras.setFont(font)
        self.btn_convertir_libras.setObjectName("btn_convertir_libras")
        self.btn_convertir_francos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_convertir_francos.setGeometry(QtCore.QRect(210, 290, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_convertir_francos.setFont(font)
        self.btn_convertir_francos.setObjectName("btn_convertir_francos")
        self.btn_convertir_yenes = QtWidgets.QPushButton(self.centralwidget)
        self.btn_convertir_yenes.setGeometry(QtCore.QRect(290, 290, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_convertir_yenes.setFont(font)
        self.btn_convertir_yenes.setObjectName("btn_convertir_yenes")
        self.btn_convertir_bolivares = QtWidgets.QPushButton(self.centralwidget)
        self.btn_convertir_bolivares.setGeometry(QtCore.QRect(370, 290, 81, 23))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btn_convertir_bolivares.setFont(font)
        self.btn_convertir_bolivares.setObjectName("btn_convertir_bolivares")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 220, 61, 61))
        self.label_3.setStyleSheet("border-image: url(iconos/USA.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 220, 61, 61))
        self.label_4.setStyleSheet("border-image: url(iconos/UK.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 220, 61, 61))
        self.label_5.setStyleSheet("border-image: url(iconos/SZ.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 220, 61, 61))
        self.label_6.setStyleSheet("border-image: url(iconos/JP.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(380, 220, 61, 61))
        self.label_7.setStyleSheet("border-image: url(iconos/VZLA.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(180, 460, 101, 81))
        self.btn_reset.setStyleSheet("border-image: url(iconos/reset.png);")
        self.btn_reset.setText("")
        self.btn_reset.setObjectName("btn_reset")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 20, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Introduce una cantidad en euros:"))
        self.label_2.setText(_translate("MainWindow", "convertir a..."))
        self.btn_convertir_dolares.setText(_translate("MainWindow", "Dólares"))
        self.btn_convertir_libras.setText(_translate("MainWindow", "Libras"))
        self.btn_convertir_francos.setText(_translate("MainWindow", "Francos"))
        self.btn_convertir_yenes.setText(_translate("MainWindow", "Yenes"))
        self.btn_convertir_bolivares.setText(_translate("MainWindow", "Bolívares"))
        self.label_8.setText(_translate("MainWindow", "CONVERSOR DE MONEDAS"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
