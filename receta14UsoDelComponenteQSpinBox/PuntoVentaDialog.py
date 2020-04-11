# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PuntoVentaDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class PuntoVentaDialog(object):
    def setupUi(self, PuntoVentaDialog):
        PuntoVentaDialog.setObjectName("PuntoVentaDialog")
        PuntoVentaDialog.resize(547, 135)
        self.lbl_producto_mouse = QtWidgets.QLabel(PuntoVentaDialog)
        self.lbl_producto_mouse.setGeometry(QtCore.QRect(20, 20, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_producto_mouse.setFont(font)
        self.lbl_producto_mouse.setObjectName("lbl_producto_mouse")
        self.lbl_producto_teclado = QtWidgets.QLabel(PuntoVentaDialog)
        self.lbl_producto_teclado.setGeometry(QtCore.QRect(20, 50, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_producto_teclado.setFont(font)
        self.lbl_producto_teclado.setObjectName("lbl_producto_teclado")
        self.lbl_gran_total = QtWidgets.QLabel(PuntoVentaDialog)
        self.lbl_gran_total.setGeometry(QtCore.QRect(400, 90, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_gran_total.setFont(font)
        self.lbl_gran_total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_gran_total.setObjectName("lbl_gran_total")
        self.txt_valor_mouse = QtWidgets.QLineEdit(PuntoVentaDialog)
        self.txt_valor_mouse.setGeometry(QtCore.QRect(160, 20, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_valor_mouse.setFont(font)
        self.txt_valor_mouse.setObjectName("txt_valor_mouse")
        self.txt_valor_teclado = QtWidgets.QLineEdit(PuntoVentaDialog)
        self.txt_valor_teclado.setGeometry(QtCore.QRect(160, 50, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_valor_teclado.setFont(font)
        self.txt_valor_teclado.setObjectName("txt_valor_teclado")
        self.sbx_cantidad_mouse = QtWidgets.QSpinBox(PuntoVentaDialog)
        self.sbx_cantidad_mouse.setGeometry(QtCore.QRect(320, 20, 61, 22))
        self.sbx_cantidad_mouse.setProperty("value", 3)
        self.sbx_cantidad_mouse.setObjectName("sbx_cantidad_mouse")
        self.sbx_cantidad_teclado = QtWidgets.QSpinBox(PuntoVentaDialog)
        self.sbx_cantidad_teclado.setGeometry(QtCore.QRect(320, 50, 61, 22))
        self.sbx_cantidad_teclado.setProperty("value", 3)
        self.sbx_cantidad_teclado.setObjectName("sbx_cantidad_teclado")
        self.txt_subtotal_mouse = QtWidgets.QLineEdit(PuntoVentaDialog)
        self.txt_subtotal_mouse.setGeometry(QtCore.QRect(400, 20, 113, 20))
        self.txt_subtotal_mouse.setObjectName("txt_subtotal_mouse")
        self.txt_subtota_teclado = QtWidgets.QLineEdit(PuntoVentaDialog)
        self.txt_subtota_teclado.setGeometry(QtCore.QRect(400, 50, 113, 20))
        self.txt_subtota_teclado.setObjectName("txt_subtota_teclado")

        self.retranslateUi(PuntoVentaDialog)
        QtCore.QMetaObject.connectSlotsByName(PuntoVentaDialog)

    def retranslateUi(self, PuntoVentaDialog):
        _translate = QtCore.QCoreApplication.translate
        PuntoVentaDialog.setWindowTitle(_translate("PuntoVentaDialog", "Punto de venta"))
        self.lbl_producto_mouse.setText(_translate("PuntoVentaDialog", "Valor mouse HyperX:"))
        self.lbl_producto_teclado.setText(_translate("PuntoVentaDialog", "Valor teclado HyperX:"))
        self.lbl_gran_total.setText(_translate("PuntoVentaDialog", "459 euros"))
        self.txt_valor_mouse.setText(_translate("PuntoVentaDialog", "60"))
        self.txt_valor_teclado.setText(_translate("PuntoVentaDialog", "93"))
        self.txt_subtotal_mouse.setText(_translate("PuntoVentaDialog", "180"))
        self.txt_subtota_teclado.setText(_translate("PuntoVentaDialog", "279"))
