# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ComidasFavoritasEditorDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class ComidasFavoritasDialog(object):
    def setupUi(self, ComidasFavoritasDialog):
        ComidasFavoritasDialog.setObjectName("ComidasFavoritasDialog")
        ComidasFavoritasDialog.resize(380, 298)
        self.lbl_agregar_comida_favorita = QtWidgets.QLabel(ComidasFavoritasDialog)
        self.lbl_agregar_comida_favorita.setGeometry(QtCore.QRect(10, 10, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_agregar_comida_favorita.setFont(font)
        self.lbl_agregar_comida_favorita.setObjectName("lbl_agregar_comida_favorita")
        self.txt_comida_favorita = QtWidgets.QLineEdit(ComidasFavoritasDialog)
        self.txt_comida_favorita.setGeometry(QtCore.QRect(170, 10, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_comida_favorita.setFont(font)
        self.txt_comida_favorita.setObjectName("txt_comida_favorita")
        self.btn_agregrar_comida_favorita = QtWidgets.QPushButton(ComidasFavoritasDialog)
        self.btn_agregrar_comida_favorita.setGeometry(QtCore.QRect(170, 40, 201, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_agregrar_comida_favorita.setFont(font)
        self.btn_agregrar_comida_favorita.setObjectName("btn_agregrar_comida_favorita")
        self.lst_comidas_favoritas = QtWidgets.QListWidget(ComidasFavoritasDialog)
        self.lst_comidas_favoritas.setGeometry(QtCore.QRect(20, 70, 351, 192))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lst_comidas_favoritas.setFont(font)
        self.lst_comidas_favoritas.setObjectName("lst_comidas_favoritas")
        self.btn_editar_comida_favorita = QtWidgets.QPushButton(ComidasFavoritasDialog)
        self.btn_editar_comida_favorita.setGeometry(QtCore.QRect(24, 270, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_editar_comida_favorita.setFont(font)
        self.btn_editar_comida_favorita.setObjectName("btn_editar_comida_favorita")
        self.btn_eliminar_comida_favorita = QtWidgets.QPushButton(ComidasFavoritasDialog)
        self.btn_eliminar_comida_favorita.setGeometry(QtCore.QRect(130, 270, 101, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_eliminar_comida_favorita.setFont(font)
        self.btn_eliminar_comida_favorita.setObjectName("btn_eliminar_comida_favorita")
        self.btn_eliminar_comidas = QtWidgets.QPushButton(ComidasFavoritasDialog)
        self.btn_eliminar_comidas.setGeometry(QtCore.QRect(250, 270, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_eliminar_comidas.setFont(font)
        self.btn_eliminar_comidas.setObjectName("btn_eliminar_comidas")

        self.retranslateUi(ComidasFavoritasDialog)
        QtCore.QMetaObject.connectSlotsByName(ComidasFavoritasDialog)

    def retranslateUi(self, ComidasFavoritasDialog):
        _translate = QtCore.QCoreApplication.translate
        ComidasFavoritasDialog.setWindowTitle(_translate("ComidasFavoritasDialog", "Comidas Favoritas"))
        self.lbl_agregar_comida_favorita.setText(_translate("ComidasFavoritasDialog", "Agregar comida favorita:"))
        self.btn_agregrar_comida_favorita.setText(_translate("ComidasFavoritasDialog", "AGREGAR"))
        self.btn_editar_comida_favorita.setText(_translate("ComidasFavoritasDialog", "EDITAR"))
        self.btn_eliminar_comida_favorita.setText(_translate("ComidasFavoritasDialog", "ELIMINAR"))
        self.btn_eliminar_comidas.setText(_translate("ComidasFavoritasDialog", "ELIMINAR TODAS"))
