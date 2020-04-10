# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogoPizza.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class PizzaDialog(object):
    def setupUi(self, PizzaDialog):
        PizzaDialog.setObjectName("PizzaDialog")
        PizzaDialog.resize(320, 240)
        self.label = QtWidgets.QLabel(PizzaDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(PizzaDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.chk_queso = QtWidgets.QCheckBox(PizzaDialog)
        self.chk_queso.setGeometry(QtCore.QRect(20, 80, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chk_queso.setFont(font)
        self.chk_queso.setObjectName("chk_queso")
        self.chk_aceitunas = QtWidgets.QCheckBox(PizzaDialog)
        self.chk_aceitunas.setGeometry(QtCore.QRect(20, 110, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chk_aceitunas.setFont(font)
        self.chk_aceitunas.setObjectName("chk_aceitunas")
        self.chk_salsas = QtWidgets.QCheckBox(PizzaDialog)
        self.chk_salsas.setGeometry(QtCore.QRect(20, 140, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chk_salsas.setFont(font)
        self.chk_salsas.setObjectName("chk_salsas")
        self.lbl_precio_final = QtWidgets.QLabel(PizzaDialog)
        self.lbl_precio_final.setGeometry(QtCore.QRect(20, 180, 281, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_precio_final.setFont(font)
        self.lbl_precio_final.setText("")
        self.lbl_precio_final.setObjectName("lbl_precio_final")

        self.retranslateUi(PizzaDialog)
        QtCore.QMetaObject.connectSlotsByName(PizzaDialog)

    def retranslateUi(self, PizzaDialog):
        _translate = QtCore.QCoreApplication.translate
        PizzaDialog.setWindowTitle(_translate("PizzaDialog", "Pizza"))
        self.label.setText(_translate("PizzaDialog", "Precio Pizza 15 euros"))
        self.label_2.setText(_translate("PizzaDialog", "Selecciona extras:"))
        self.chk_queso.setText(_translate("PizzaDialog", "Queso"))
        self.chk_aceitunas.setText(_translate("PizzaDialog", "Aceitunas"))
        self.chk_salsas.setText(_translate("PizzaDialog", "Salsas"))
