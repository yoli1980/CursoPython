# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DiagnosticosDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class DiagnosticosDialog(object):
    def setupUi(self, DiagnosticosDialog):
        DiagnosticosDialog.setObjectName("DiagnosticosDialog")
        DiagnosticosDialog.resize(311, 211)
        font = QtGui.QFont()
        font.setPointSize(10)
        DiagnosticosDialog.setFont(font)
        self.lbl_seleccion_diagnostico = QtWidgets.QLabel(DiagnosticosDialog)
        self.lbl_seleccion_diagnostico.setGeometry(QtCore.QRect(30, 10, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_seleccion_diagnostico.setFont(font)
        self.lbl_seleccion_diagnostico.setObjectName("lbl_seleccion_diagnostico")
        self.lbl_resultado = QtWidgets.QLabel(DiagnosticosDialog)
        self.lbl_resultado.setGeometry(QtCore.QRect(30, 150, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_resultado.setFont(font)
        self.lbl_resultado.setObjectName("lbl_resultado")
        self.lst_diagnosticos = QtWidgets.QListWidget(DiagnosticosDialog)
        self.lst_diagnosticos.setGeometry(QtCore.QRect(30, 30, 256, 101))
        self.lst_diagnosticos.setObjectName("lst_diagnosticos")
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos.addItem(item)

        self.retranslateUi(DiagnosticosDialog)
        QtCore.QMetaObject.connectSlotsByName(DiagnosticosDialog)

    def retranslateUi(self, DiagnosticosDialog):
        _translate = QtCore.QCoreApplication.translate
        DiagnosticosDialog.setWindowTitle(_translate("DiagnosticosDialog", "Diagnósticos"))
        self.lbl_seleccion_diagnostico.setText(_translate("DiagnosticosDialog", "Seleccione el diagnóstico:"))
        self.lbl_resultado.setText(_translate("DiagnosticosDialog", " "))
        __sortingEnabled = self.lst_diagnosticos.isSortingEnabled()
        self.lst_diagnosticos.setSortingEnabled(False)
        item = self.lst_diagnosticos.item(0)
        item.setText(_translate("DiagnosticosDialog", "Rayos X 5 - euros"))
        item = self.lst_diagnosticos.item(1)
        item.setText(_translate("DiagnosticosDialog", "Nivel de azúcar - 3 euros"))
        item = self.lst_diagnosticos.item(2)
        item.setText(_translate("DiagnosticosDialog", "Prueba de hemoglobina - 7 euros"))
        item = self.lst_diagnosticos.item(3)
        item.setText(_translate("DiagnosticosDialog", "Análisis de orina - 8 euros"))
        item = self.lst_diagnosticos.item(4)
        item.setText(_translate("DiagnosticosDialog", "Análisis del PSA - 10 euros"))
        self.lst_diagnosticos.setSortingEnabled(__sortingEnabled)
