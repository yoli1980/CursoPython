# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LenguajesProgramacionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class LenguajeProgamacionFavoritoDialog(object):
    def setupUi(self, LenguajeProgamacionFavoritoDialog):
        LenguajeProgamacionFavoritoDialog.setObjectName("LenguajeProgamacionFavoritoDialog")
        LenguajeProgamacionFavoritoDialog.resize(479, 117)
        font = QtGui.QFont()
        font.setPointSize(10)
        LenguajeProgamacionFavoritoDialog.setFont(font)
        self.lbl_seleccione_lenguaje = QtWidgets.QLabel(LenguajeProgamacionFavoritoDialog)
        self.lbl_seleccione_lenguaje.setGeometry(QtCore.QRect(10, 10, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_seleccione_lenguaje.setFont(font)
        self.lbl_seleccione_lenguaje.setObjectName("lbl_seleccione_lenguaje")
        self.lbl_lenguaje_seleccionado = QtWidgets.QLabel(LenguajeProgamacionFavoritoDialog)
        self.lbl_lenguaje_seleccionado.setGeometry(QtCore.QRect(20, 60, 431, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_lenguaje_seleccionado.setFont(font)
        self.lbl_lenguaje_seleccionado.setText("")
        self.lbl_lenguaje_seleccionado.setObjectName("lbl_lenguaje_seleccionado")
        self.cbx_lenguajes = QtWidgets.QComboBox(LenguajeProgamacionFavoritoDialog)
        self.cbx_lenguajes.setGeometry(QtCore.QRect(260, 10, 211, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbx_lenguajes.setFont(font)
        self.cbx_lenguajes.setObjectName("cbx_lenguajes")
        self.cbx_lenguajes.addItem("")
        self.cbx_lenguajes.addItem("")
        self.cbx_lenguajes.addItem("")
        self.cbx_lenguajes.addItem("")
        self.cbx_lenguajes.addItem("")
        self.cbx_lenguajes.addItem("")

        self.retranslateUi(LenguajeProgamacionFavoritoDialog)
        QtCore.QMetaObject.connectSlotsByName(LenguajeProgamacionFavoritoDialog)

    def retranslateUi(self, LenguajeProgamacionFavoritoDialog):
        _translate = QtCore.QCoreApplication.translate
        LenguajeProgamacionFavoritoDialog.setWindowTitle(_translate("LenguajeProgamacionFavoritoDialog", "Lenguajes de Programación"))
        self.lbl_seleccione_lenguaje.setText(_translate("LenguajeProgamacionFavoritoDialog", "Seleccione lenguaje de programación:"))
        self.cbx_lenguajes.setItemText(0, _translate("LenguajeProgamacionFavoritoDialog", "Python"))
        self.cbx_lenguajes.setItemText(1, _translate("LenguajeProgamacionFavoritoDialog", "Java"))
        self.cbx_lenguajes.setItemText(2, _translate("LenguajeProgamacionFavoritoDialog", "C#"))
        self.cbx_lenguajes.setItemText(3, _translate("LenguajeProgamacionFavoritoDialog", "PHP"))
        self.cbx_lenguajes.setItemText(4, _translate("LenguajeProgamacionFavoritoDialog", "JavaScript"))
        self.cbx_lenguajes.setItemText(5, _translate("LenguajeProgamacionFavoritoDialog", "C++"))
