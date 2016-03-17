# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QPackage_dialog_base.ui'
#
# Created: Thu Mar 17 17:05:23 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_QPackageDialogBase(object):
    def setupUi(self, QPackageDialogBase):
        QPackageDialogBase.setObjectName(_fromUtf8("QPackageDialogBase"))
        QPackageDialogBase.resize(544, 507)
        self._repertoire = QtGui.QTextEdit(QPackageDialogBase)
        self._repertoire.setGeometry(QtCore.QRect(60, 350, 311, 21))
        self._repertoire.setObjectName(_fromUtf8("_repertoire"))
        self._repertoire_boutton = QtGui.QPushButton(QPackageDialogBase)
        self._repertoire_boutton.setGeometry(QtCore.QRect(380, 350, 151, 23))
        self._repertoire_boutton.setObjectName(_fromUtf8("_repertoire_boutton"))
        self._tableau = QtGui.QTableView(QPackageDialogBase)
        self._tableau.setGeometry(QtCore.QRect(30, 40, 501, 291))
        self._tableau.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self._tableau.setAlternatingRowColors(True)
        self._tableau.setSortingEnabled(True)
        self._tableau.setObjectName(_fromUtf8("_tableau"))
        self._tableau.horizontalHeader().setDefaultSectionSize(1000)
        self._charger = QtGui.QPushButton(QPackageDialogBase)
        self._charger.setGeometry(QtCore.QRect(150, 10, 241, 23))
        self._charger.setObjectName(_fromUtf8("_charger"))
        self._copy = QtGui.QPushButton(QPackageDialogBase)
        self._copy.setGeometry(QtCore.QRect(130, 430, 281, 23))
        self._copy.setObjectName(_fromUtf8("_copy"))
        self._listeprojections = QtGui.QComboBox(QPackageDialogBase)
        self._listeprojections.setGeometry(QtCore.QRect(270, 390, 131, 22))
        self._listeprojections.setEditable(True)
        self._listeprojections.setObjectName(_fromUtf8("_listeprojections"))
        self.label = QtGui.QLabel(QPackageDialogBase)
        self.label.setGeometry(QtCore.QRect(150, 390, 111, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self._progression = QtGui.QProgressBar(QPackageDialogBase)
        self._progression.setGeometry(QtCore.QRect(20, 470, 521, 23))
        self._progression.setProperty("value", 0)
        self._progression.setObjectName(_fromUtf8("_progression"))

        self.retranslateUi(QPackageDialogBase)
        QtCore.QObject.connect(self._repertoire_boutton, QtCore.SIGNAL(_fromUtf8("clicked()")), QPackageDialogBase.chercherRepertoire)
        QtCore.QObject.connect(self._charger, QtCore.SIGNAL(_fromUtf8("clicked()")), QPackageDialogBase.chargerCouches)
        QtCore.QObject.connect(self._copy, QtCore.SIGNAL(_fromUtf8("clicked()")), QPackageDialogBase.copierCouches)
        QtCore.QMetaObject.connectSlotsByName(QPackageDialogBase)

    def retranslateUi(self, QPackageDialogBase):
        QPackageDialogBase.setWindowTitle(_translate("QPackageDialogBase", "QPackage", None))
        self._repertoire_boutton.setText(_translate("QPackageDialogBase", "Destination folder", None))
        self._charger.setText(_translate("QPackageDialogBase", "Load layers of the current project", None))
        self._copy.setText(_translate("QPackageDialogBase", "Copy the layers", None))
        self.label.setText(_translate("QPackageDialogBase", "Choose the CRS", None))

