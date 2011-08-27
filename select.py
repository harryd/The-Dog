# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_parts.ui'
#
# Created: Fri Aug 26 21:43:01 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dlgParts(object):
    def setupUi(self, dlgParts):
        dlgParts.setObjectName(_fromUtf8("dlgParts"))
        dlgParts.resize(380, 280)
        dlgParts.setWindowTitle(QtGui.QApplication.translate("dlgParts", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBox = QtGui.QDialogButtonBox(dlgParts)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(dlgParts)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 215))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblItems = QtGui.QLabel(self.layoutWidget)
        self.lblItems.setText(QtGui.QApplication.translate("dlgParts", "Items", None, QtGui.QApplication.UnicodeUTF8))
        self.lblItems.setObjectName(_fromUtf8("lblItems"))
        self.gridLayout.addWidget(self.lblItems, 0, 0, 1, 1)
        self.lblPrices = QtGui.QLabel(self.layoutWidget)
        self.lblPrices.setText(QtGui.QApplication.translate("dlgParts", "Prices", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPrices.setObjectName(_fromUtf8("lblPrices"))
        self.gridLayout.addWidget(self.lblPrices, 0, 1, 1, 1)
        self.lstItems = QtGui.QListWidget(self.layoutWidget)
        self.lstItems.setObjectName(_fromUtf8("lstItems"))
        self.gridLayout.addWidget(self.lstItems, 1, 0, 2, 1)
        self.lstPrices = QtGui.QListWidget(self.layoutWidget)
        self.lstPrices.setObjectName(_fromUtf8("lstPrices"))
        self.gridLayout.addWidget(self.lstPrices, 1, 1, 1, 1)
        self.txtPrice = QtGui.QLineEdit(self.layoutWidget)
        self.txtPrice.setObjectName(_fromUtf8("txtPrice"))
        self.gridLayout.addWidget(self.txtPrice, 2, 1, 1, 1)
        self.lblItems.setBuddy(self.lstItems)
        self.lblPrices.setBuddy(self.lstItems)

        self.retranslateUi(dlgParts)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), dlgParts.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), dlgParts.reject)
        QtCore.QObject.connect(self.lstItems, QtCore.SIGNAL(_fromUtf8("doubleClicked(QModelIndex)")), self.lstPrices.setFocus)
        QtCore.QObject.connect(self.lstItems, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), self.lstPrices.setFocus)
        QtCore.QObject.connect(self.txtPrice, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.lstPrices.setFocus)
        QtCore.QMetaObject.connectSlotsByName(dlgParts)

    def retranslateUi(self, dlgParts):
        self.lstItems.setSortingEnabled(True)

