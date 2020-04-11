# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalculadoraDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class CalculadoraDialog(object):
    def setupUi(self, CalculadoraDialog):
        CalculadoraDialog.setObjectName("CalculadoraDialog")
        CalculadoraDialog.resize(299, 240)
        self.label = QtWidgets.QLabel(CalculadoraDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(CalculadoraDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_primer_numero = QtWidgets.QLineEdit(CalculadoraDialog)
        self.txt_primer_numero.setGeometry(QtCore.QRect(170, 20, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_primer_numero.setFont(font)
        self.txt_primer_numero.setObjectName("txt_primer_numero")
        self.txt_segundo_numero = QtWidgets.QLineEdit(CalculadoraDialog)
        self.txt_segundo_numero.setGeometry(QtCore.QRect(170, 60, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_segundo_numero.setFont(font)
        self.txt_segundo_numero.setObjectName("txt_segundo_numero")
        self.btn_sumar = QtWidgets.QPushButton(CalculadoraDialog)
        self.btn_sumar.setGeometry(QtCore.QRect(30, 110, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_sumar.setFont(font)
        self.btn_sumar.setObjectName("btn_sumar")
        self.btn_restar = QtWidgets.QPushButton(CalculadoraDialog)
        self.btn_restar.setGeometry(QtCore.QRect(90, 110, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_restar.setFont(font)
        self.btn_restar.setObjectName("btn_restar")
        self.btn_multiplicar = QtWidgets.QPushButton(CalculadoraDialog)
        self.btn_multiplicar.setGeometry(QtCore.QRect(150, 110, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_multiplicar.setFont(font)
        self.btn_multiplicar.setObjectName("btn_multiplicar")
        self.btn_dividir = QtWidgets.QPushButton(CalculadoraDialog)
        self.btn_dividir.setGeometry(QtCore.QRect(210, 110, 51, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_dividir.setFont(font)
        self.btn_dividir.setObjectName("btn_dividir")
        self.lbl_resultado = QtWidgets.QLabel(CalculadoraDialog)
        self.lbl_resultado.setGeometry(QtCore.QRect(50, 170, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_resultado.setFont(font)
        self.lbl_resultado.setText("")
        self.lbl_resultado.setObjectName("lbl_resultado")

        self.retranslateUi(CalculadoraDialog)
        QtCore.QMetaObject.connectSlotsByName(CalculadoraDialog)

    def retranslateUi(self, CalculadoraDialog):
        _translate = QtCore.QCoreApplication.translate
        CalculadoraDialog.setWindowTitle(_translate("CalculadoraDialog", "Calculadora"))
        self.label.setText(_translate("CalculadoraDialog", "Ingrese primer número:"))
        self.label_2.setText(_translate("CalculadoraDialog", "Ingrese segundo número:"))
        self.btn_sumar.setText(_translate("CalculadoraDialog", "+"))
        self.btn_restar.setText(_translate("CalculadoraDialog", "-"))
        self.btn_multiplicar.setText(_translate("CalculadoraDialog", "x"))
        self.btn_dividir.setText(_translate("CalculadoraDialog", "/"))
