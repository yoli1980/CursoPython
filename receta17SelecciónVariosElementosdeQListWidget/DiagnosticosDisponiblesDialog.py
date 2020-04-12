# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DiagnosticosDisponiblesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class DiagnosticoSeleccionDialog(object):
    def setupUi(self, DiagnosticoSeleccionDialog):
        DiagnosticoSeleccionDialog.setObjectName("DiagnosticoSeleccionDialog")
        DiagnosticoSeleccionDialog.resize(527, 437)
        self.lbl_diagnosticos_disponibles = QtWidgets.QLabel(DiagnosticoSeleccionDialog)
        self.lbl_diagnosticos_disponibles.setGeometry(QtCore.QRect(10, 20, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_diagnosticos_disponibles.setFont(font)
        self.lbl_diagnosticos_disponibles.setObjectName("lbl_diagnosticos_disponibles")
        self.lbl_diagnosticos_seleccionados = QtWidgets.QLabel(DiagnosticoSeleccionDialog)
        self.lbl_diagnosticos_seleccionados.setGeometry(QtCore.QRect(10, 210, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_diagnosticos_seleccionados.setFont(font)
        self.lbl_diagnosticos_seleccionados.setObjectName("lbl_diagnosticos_seleccionados")
        self.lst_diagnosticos_disponibles = QtWidgets.QListWidget(DiagnosticoSeleccionDialog)
        self.lst_diagnosticos_disponibles.setGeometry(QtCore.QRect(180, 20, 331, 192))
        self.lst_diagnosticos_disponibles.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.lst_diagnosticos_disponibles.setObjectName("lst_diagnosticos_disponibles")
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos_disponibles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos_disponibles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos_disponibles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos_disponibles.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.lst_diagnosticos_disponibles.addItem(item)
        self.lst_diagnosticos_seleccionados = QtWidgets.QListWidget(DiagnosticoSeleccionDialog)
        self.lst_diagnosticos_seleccionados.setGeometry(QtCore.QRect(180, 230, 331, 192))
        self.lst_diagnosticos_seleccionados.setObjectName("lst_diagnosticos_seleccionados")

        self.retranslateUi(DiagnosticoSeleccionDialog)
        QtCore.QMetaObject.connectSlotsByName(DiagnosticoSeleccionDialog)

    def retranslateUi(self, DiagnosticoSeleccionDialog):
        _translate = QtCore.QCoreApplication.translate
        DiagnosticoSeleccionDialog.setWindowTitle(_translate("DiagnosticoSeleccionDialog", "Selección de Diagnósticos"))
        self.lbl_diagnosticos_disponibles.setText(_translate("DiagnosticoSeleccionDialog", "Diagnósticos disponibles:"))
        self.lbl_diagnosticos_seleccionados.setText(_translate("DiagnosticoSeleccionDialog", "Diagnósticos seleccionados:"))
        __sortingEnabled = self.lst_diagnosticos_disponibles.isSortingEnabled()
        self.lst_diagnosticos_disponibles.setSortingEnabled(False)
        item = self.lst_diagnosticos_disponibles.item(0)
        item.setText(_translate("DiagnosticoSeleccionDialog", "Rayos X - 5 euros"))
        item = self.lst_diagnosticos_disponibles.item(1)
        item.setText(_translate("DiagnosticoSeleccionDialog", "Nivel de azúcar - 3 euros"))
        item = self.lst_diagnosticos_disponibles.item(2)
        item.setText(_translate("DiagnosticoSeleccionDialog", "Prueba de hemoglobina - 7 euros"))
        item = self.lst_diagnosticos_disponibles.item(3)
        item.setText(_translate("DiagnosticoSeleccionDialog", "Análisis de orina - 8 euros"))
        item = self.lst_diagnosticos_disponibles.item(4)
        item.setText(_translate("DiagnosticoSeleccionDialog", "Análisis del PSA - 10 euros"))
        self.lst_diagnosticos_disponibles.setSortingEnabled(__sortingEnabled)
