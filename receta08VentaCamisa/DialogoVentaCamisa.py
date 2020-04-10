# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogoVentaCamisa.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class DialogoVentaCamisa(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 365)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 160, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vly_tallas = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vly_tallas.setContentsMargins(0, 0, 0, 0)
        self.vly_tallas.setObjectName("vly_tallas")
        self.rbtn_xs = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbtn_xs.setObjectName("rbtn_xs")
        self.vly_tallas.addWidget(self.rbtn_xs)
        self.rbtn_s = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbtn_s.setObjectName("rbtn_s")
        self.vly_tallas.addWidget(self.rbtn_s)
        self.rbtn_m = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbtn_m.setObjectName("rbtn_m")
        self.vly_tallas.addWidget(self.rbtn_m)
        self.rbtn_l = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbtn_l.setObjectName("rbtn_l")
        self.vly_tallas.addWidget(self.rbtn_l)
        self.rbtn_xl = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbtn_xl.setObjectName("rbtn_xl")
        self.vly_tallas.addWidget(self.rbtn_xl)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 160, 160, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.vly_metodo_pago = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vly_metodo_pago.setContentsMargins(0, 0, 0, 0)
        self.vly_metodo_pago.setObjectName("vly_metodo_pago")
        self.rbtn_debito_credito = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbtn_debito_credito.setObjectName("rbtn_debito_credito")
        self.vly_metodo_pago.addWidget(self.rbtn_debito_credito)
        self.rbtn_contrareembolso = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbtn_contrareembolso.setObjectName("rbtn_contrareembolso")
        self.vly_metodo_pago.addWidget(self.rbtn_contrareembolso)
        self.rbtn_transferencia_bancaria = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbtn_transferencia_bancaria.setObjectName("rbtn_transferencia_bancaria")
        self.vly_metodo_pago.addWidget(self.rbtn_transferencia_bancaria)
        self.lbl_resultado_seleccion = QtWidgets.QLabel(Dialog)
        self.lbl_resultado_seleccion.setGeometry(QtCore.QRect(10, 260, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_resultado_seleccion.setFont(font)
        self.lbl_resultado_seleccion.setText("")
        self.lbl_resultado_seleccion.setObjectName("lbl_resultado_seleccion")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Venta"))
        self.label.setText(_translate("Dialog", "Elige la talla:"))
        self.label_2.setText(_translate("Dialog", "Elige el método de pago:"))
        self.rbtn_xs.setText(_translate("Dialog", "XS"))
        self.rbtn_s.setText(_translate("Dialog", "S"))
        self.rbtn_m.setText(_translate("Dialog", "M"))
        self.rbtn_l.setText(_translate("Dialog", "L"))
        self.rbtn_xl.setText(_translate("Dialog", "XL"))
        self.rbtn_debito_credito.setText(_translate("Dialog", "Tarjeta débito/crédito"))
        self.rbtn_contrareembolso.setText(_translate("Dialog", "Contrareembolso"))
        self.rbtn_transferencia_bancaria.setText(_translate("Dialog", "Transferencia bancaria"))
