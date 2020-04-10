# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogoClaseVuelo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class DialogoClaseVuelo(object):
    def setupUi(self, DialogoClaseVuelo):
        DialogoClaseVuelo.setObjectName("DialogoClaseVuelo")
        DialogoClaseVuelo.resize(320, 240)
        self.label = QtWidgets.QLabel(DialogoClaseVuelo)
        self.label.setGeometry(QtCore.QRect(20, 20, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.rbtn_primera_clase = QtWidgets.QRadioButton(DialogoClaseVuelo)
        self.rbtn_primera_clase.setGeometry(QtCore.QRect(20, 50, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbtn_primera_clase.setFont(font)
        self.rbtn_primera_clase.setObjectName("rbtn_primera_clase")
        self.rbtn_clase_negocios = QtWidgets.QRadioButton(DialogoClaseVuelo)
        self.rbtn_clase_negocios.setGeometry(QtCore.QRect(20, 80, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbtn_clase_negocios.setFont(font)
        self.rbtn_clase_negocios.setObjectName("rbtn_clase_negocios")
        self.rbtn_clase_economica = QtWidgets.QRadioButton(DialogoClaseVuelo)
        self.rbtn_clase_economica.setGeometry(QtCore.QRect(20, 110, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbtn_clase_economica.setFont(font)
        self.rbtn_clase_economica.setObjectName("rbtn_clase_economica")
        self.lbl_resultado_seleccion = QtWidgets.QLabel(DialogoClaseVuelo)
        self.lbl_resultado_seleccion.setGeometry(QtCore.QRect(20, 160, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbl_resultado_seleccion.setFont(font)
        self.lbl_resultado_seleccion.setText("")
        self.lbl_resultado_seleccion.setObjectName("lbl_resultado_seleccion")

        self.retranslateUi(DialogoClaseVuelo)
        QtCore.QMetaObject.connectSlotsByName(DialogoClaseVuelo)

    def retranslateUi(self, DialogoClaseVuelo):
        _translate = QtCore.QCoreApplication.translate
        DialogoClaseVuelo.setWindowTitle(_translate("DialogoClaseVuelo", "Clase Vuelo"))
        self.label.setText(_translate("DialogoClaseVuelo", "Escoja la clase del Vuelo:"))
        self.rbtn_primera_clase.setText(_translate("DialogoClaseVuelo", "Primera clase:"))
        self.rbtn_clase_negocios.setText(_translate("DialogoClaseVuelo", "Clase negocios:"))
        self.rbtn_clase_economica.setText(_translate("DialogoClaseVuelo", "Clase económica:"))
