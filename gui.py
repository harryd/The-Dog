# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Aug 11 01:08:21 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_winMain(object):
    def setupUi(self, winMain):
        winMain.setObjectName(_fromUtf8("winMain"))
        winMain.resize(760, 644)
        self.centralwidget = QtGui.QWidget(winMain)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setSizeIncrement(QtCore.QSize(1, 1))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tblMain = QtGui.QTableWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.tblMain.sizePolicy().hasHeightForWidth())
        self.tblMain.setSizePolicy(sizePolicy)
        self.tblMain.setSizeIncrement(QtCore.QSize(1, 1))
        self.tblMain.setAutoFillBackground(True)
        self.tblMain.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblMain.setAlternatingRowColors(True)
        self.tblMain.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblMain.setObjectName(_fromUtf8("tblMain"))
        self.tblMain.setColumnCount(5)
        self.tblMain.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tblMain.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblMain.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblMain.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblMain.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tblMain.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tblMain.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.tblMain.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.tblMain.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.tblMain.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.tblMain.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tblMain.setItem(0, 4, item)
        self.tblMain.horizontalHeader().setCascadingSectionResizes(True)
        self.tblMain.horizontalHeader().setDefaultSectionSize(100)
        self.tblMain.horizontalHeader().setStretchLastSection(False)
        self.gridLayout_2.addWidget(self.tblMain, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnClear = QtGui.QPushButton(self.frame)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.horizontalLayout.addWidget(self.btnClear)
        self.btnDone = QtGui.QPushButton(self.frame)
        self.btnDone.setObjectName(_fromUtf8("btnDone"))
        self.horizontalLayout.addWidget(self.btnDone)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        winMain.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(winMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        winMain.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(winMain)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        winMain.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(winMain)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.btnClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.tblMain.clearContents)
        QtCore.QMetaObject.connectSlotsByName(winMain)

    def retranslateUi(self, winMain):
        winMain.setWindowTitle(QtGui.QApplication.translate("winMain", "Laughing dog", None, QtGui.QApplication.UnicodeUTF8))
        self.tblMain.verticalHeaderItem(0).setText(QtGui.QApplication.translate("winMain", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.tblMain.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("winMain", "Item", None, QtGui.QApplication.UnicodeUTF8))
        self.tblMain.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("winMain", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.tblMain.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("winMain", "Price", None, QtGui.QApplication.UnicodeUTF8))
        self.tblMain.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("winMain", "Qty", None, QtGui.QApplication.UnicodeUTF8))
        self.tblMain.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("winMain", "Total", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.tblMain.isSortingEnabled()
        self.tblMain.setSortingEnabled(False)
        self.tblMain.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("winMain", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("winMain", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClear.setText(QtGui.QApplication.translate("winMain", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDone.setText(QtGui.QApplication.translate("winMain", "Done", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("winMain", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("winMain", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("winMain", "Settings", None, QtGui.QApplication.UnicodeUTF8))

