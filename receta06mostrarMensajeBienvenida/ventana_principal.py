# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogoSaludar(object):
    def setupUi(self, DialogoSaludar):
        DialogoSaludar.setObjectName("DialogoSaludar")
        DialogoSaludar.resize(320, 240)
        self.centralwidget = QtWidgets.QWidget(DialogoSaludar)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_escriba_su_nombre = QtWidgets.QLabel(self.centralwidget)
        self.lbl_escriba_su_nombre.setGeometry(QtCore.QRect(10, 30, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_escriba_su_nombre.setFont(font)
        self.lbl_escriba_su_nombre.setObjectName("lbl_escriba_su_nombre")
        self.txt_nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nombre.setGeometry(QtCore.QRect(160, 30, 151, 20))
        self.txt_nombre.setObjectName("txt_nombre")
        self.lbl_saludo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_saludo.setGeometry(QtCore.QRect(10, 100, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_saludo.setFont(font)
        self.lbl_saludo.setObjectName("lbl_saludo")
        self.lbl_mensaje_saludo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mensaje_saludo.setGeometry(QtCore.QRect(160, 100, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_mensaje_saludo.setFont(font)
        self.lbl_mensaje_saludo.setText("")
        self.lbl_mensaje_saludo.setObjectName("lbl_mensaje_saludo")
        self.btn_saludar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_saludar.setGeometry(QtCore.QRect(90, 170, 131, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_saludar.setFont(font)
        self.btn_saludar.setObjectName("btn_saludar")
        DialogoSaludar.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DialogoSaludar)
        self.statusbar.setObjectName("statusbar")
        DialogoSaludar.setStatusBar(self.statusbar)

        self.retranslateUi(DialogoSaludar)
        QtCore.QMetaObject.connectSlotsByName(DialogoSaludar)

    def retranslateUi(self, DialogoSaludar):
        _translate = QtCore.QCoreApplication.translate
        DialogoSaludar.setWindowTitle(_translate("DialogoSaludar", "Saludo"))
        self.lbl_escriba_su_nombre.setText(_translate("DialogoSaludar", "Escriba su nombre:"))
        self.lbl_saludo.setText(_translate("DialogoSaludar", "Saludo:"))
        self.btn_saludar.setText(_translate("DialogoSaludar", "SALUDAR"))
