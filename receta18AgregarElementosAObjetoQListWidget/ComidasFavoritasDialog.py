# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ComidasFavoritasDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class ComidasFavoritasDialog(object):
    def setupUi(self, ComidasFavoritasDialog):
        ComidasFavoritasDialog.setObjectName("ComidasFavoritasDialog")
        ComidasFavoritasDialog.resize(428, 249)
        self.lbl_comida_favorita = QtWidgets.QLabel(ComidasFavoritasDialog)
        self.lbl_comida_favorita.setGeometry(QtCore.QRect(10, 20, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_comida_favorita.setFont(font)
        self.lbl_comida_favorita.setObjectName("lbl_comida_favorita")
        self.txt_comida_favorita = QtWidgets.QLineEdit(ComidasFavoritasDialog)
        self.txt_comida_favorita.setGeometry(QtCore.QRect(180, 20, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_comida_favorita.setFont(font)
        self.txt_comida_favorita.setObjectName("txt_comida_favorita")
        self.btn_agregar_comida = QtWidgets.QPushButton(ComidasFavoritasDialog)
        self.btn_agregar_comida.setGeometry(QtCore.QRect(240, 50, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_agregar_comida.setFont(font)
        self.btn_agregar_comida.setObjectName("btn_agregar_comida")
        self.lst_comidas_favoritas = QtWidgets.QListWidget(ComidasFavoritasDialog)
        self.lst_comidas_favoritas.setGeometry(QtCore.QRect(15, 90, 401, 141))
        self.lst_comidas_favoritas.setObjectName("lst_comidas_favoritas")

        self.retranslateUi(ComidasFavoritasDialog)
        QtCore.QMetaObject.connectSlotsByName(ComidasFavoritasDialog)

    def retranslateUi(self, ComidasFavoritasDialog):
        _translate = QtCore.QCoreApplication.translate
        ComidasFavoritasDialog.setWindowTitle(_translate("ComidasFavoritasDialog", "Comidas Favoritas"))
        self.lbl_comida_favorita.setText(_translate("ComidasFavoritasDialog", "Agregar comida favorita:"))
        self.btn_agregar_comida.setText(_translate("ComidasFavoritasDialog", "AGREGAR"))
