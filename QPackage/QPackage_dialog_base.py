# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QPackage_dialog_base.ui'
#
# Created: Sat Mar 26 17:13:17 2016
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
        QPackageDialogBase.resize(492, 591)
        self.verticalLayout_2 = QtGui.QVBoxLayout(QPackageDialogBase)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self._charger = QtGui.QPushButton(QPackageDialogBase)
        self._charger.setObjectName(_fromUtf8("_charger"))
        self.horizontalLayout_3.addWidget(self._charger)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self._tableau = QtGui.QTableView(QPackageDialogBase)
        self._tableau.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self._tableau.setAlternatingRowColors(True)
        self._tableau.setSortingEnabled(True)
        self._tableau.setObjectName(_fromUtf8("_tableau"))
        self._tableau.horizontalHeader().setDefaultSectionSize(1000)
        self.verticalLayout.addWidget(self._tableau)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self._repertoire = QtGui.QLineEdit(QPackageDialogBase)
        self._repertoire.setObjectName(_fromUtf8("_repertoire"))
        self.horizontalLayout.addWidget(self._repertoire)
        self._repertoire_boutton = QtGui.QPushButton(QPackageDialogBase)
        self._repertoire_boutton.setObjectName(_fromUtf8("_repertoire_boutton"))
        self.horizontalLayout.addWidget(self._repertoire_boutton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_2 = QtGui.QLabel(QPackageDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self._projectname = QtGui.QLineEdit(QPackageDialogBase)
        self._projectname.setText(_fromUtf8(""))
        self._projectname.setObjectName(_fromUtf8("_projectname"))
        self.horizontalLayout_5.addWidget(self._projectname)
        self.label_3 = QtGui.QLabel(QPackageDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(QPackageDialogBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self._listeprojections = QtGui.QComboBox(QPackageDialogBase)
        self._listeprojections.setEditable(True)
        self._listeprojections.setObjectName(_fromUtf8("_listeprojections"))
        self.horizontalLayout_2.addWidget(self._listeprojections)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self._copy = QtGui.QPushButton(QPackageDialogBase)
        self._copy.setObjectName(_fromUtf8("_copy"))
        self.horizontalLayout_4.addWidget(self._copy)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self._progression = QtGui.QProgressBar(QPackageDialogBase)
        self._progression.setProperty("value", 0)
        self._progression.setObjectName(_fromUtf8("_progression"))
        self.verticalLayout.addWidget(self._progression)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(QPackageDialogBase)
        QtCore.QObject.connect(self._repertoire_boutton, QtCore.SIGNAL(_fromUtf8("clicked()")), QPackageDialogBase.chercherRepertoire)
        QtCore.QObject.connect(self._charger, QtCore.SIGNAL(_fromUtf8("clicked()")), QPackageDialogBase.chargerCouches)
        QtCore.QObject.connect(self._copy, QtCore.SIGNAL(_fromUtf8("clicked()")), QPackageDialogBase.copierCouches)
        QtCore.QMetaObject.connectSlotsByName(QPackageDialogBase)

    def retranslateUi(self, QPackageDialogBase):
        QPackageDialogBase.setWindowTitle(_translate("QPackageDialogBase", "QPackage", None))
        self._charger.setText(_translate("QPackageDialogBase", "Load layers of the current project", None))
        self._repertoire_boutton.setText(_translate("QPackageDialogBase", "Destination folder", None))
        self.label_2.setText(_translate("QPackageDialogBase", "Project name : ", None))
        self.label_3.setText(_translate("QPackageDialogBase", "(.qgs)", None))
        self.label.setText(_translate("QPackageDialogBase", "Choose the CRS : ", None))
        self._copy.setText(_translate("QPackageDialogBase", "Copy the layers", None))

