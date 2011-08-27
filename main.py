#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
from gui import Ui_winMain
from select import Ui_dlgParts
prices = {  'tubes': ["$6.00",  "$7.00",  "$6.50"], 
            'tires': ["$30.00", "$40.00", "$20.00"],
            'misc':  ["$10.00", "$20.00", "$50.00"]
            }

class SelectParts(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.ui = Ui_dlgParts()
        self.ui.setupUi(self)
        self.ui.lstItems.addItems([k for k,v in prices.iteritems()])
        self.ui.lstItems.setCurrentRow(0)
        self.ui.lstItems.setFocus()
        self.set_prices(self.ui.lstItems.currentItem())
        self.item = None
        self.price = None
        self.done = False
        QObject.connect(self.ui.lstItems, SIGNAL("itemClicked(QListWidgetItem*)"), self.set_prices)
        QObject.connect(self.ui.txtPrice, SIGNAL("returnPressed()"), self.price_entered)
        QObject.connect(self.ui.txtPrice, SIGNAL("textEdited(const QString&)"), self.price_entered)

    def price_entered(self, price=None):
        print price

    def advance(self):
        if self.ui.lstItems.hasFocus():
            pass
            #self.ui.txtPrice.setFocus()
        else:
            print "What"

    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == Qt.Key_Return:
            self.advance()

    def get_prices(self, item):
        text = str(item.text())
        if text in prices:
            return prices[text]
        else:
            return []

    def set_prices(self, item):
        self.ui.lstPrices.clear()
        self.ui.lstPrices.addItems(self.get_prices(item))

    def accept(self):
        if self.ui.lstPrices.currentItem() != None:
            self.done = True
            self.item = self.ui.lstItems.currentItem().text()
            self.price = self.ui.lstPrices.currentItem().text()

        #self.emit(SIGNAL("acceptedItem(item, price)"), self.item, self.price)
        QDialog.accept(self)


class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_winMain()
        self.ui.setupUi(self)
        self.itemProto = QTableWidgetItem()
        self.itemProto.setFlags(Qt.NoItemFlags)
        self.ui.tblMain.setItemPrototype(self.itemProto)
        self.ui.tblMain.insertRow(self.ui.tblMain.rowCount() - 1)
        QObject.connect(self.ui.tblMain, SIGNAL("currentCellChanged(int,int,int,int)"), self.cellChanged)
    
    def is_int(self, s):
        try: 
            int(s)
            return True
        except ValueError:
            return False
    
    def keyPressEvent(self, keyEvent):
        if keyEvent.key() == Qt.Key_Return:
            self.advance()
    
    def cellChanged(self, row, column, prev_row, prev_column):
        item = self.ui.tblMain.item(row, column)
        if column == 0:
            dlg = SelectParts(self)
            dlg.exec_()
            if not dlg.done:
                self.ui.tblMain.setCurrentCell(row, 0)
                return
            self.ui.tblMain.setItem(row, 0, QTableWidgetItem(dlg.item))
            self.ui.tblMain.setItem(row, 2, QTableWidgetItem(dlg.price))
            self.ui.tblMain.setItem(row, 3, QTableWidgetItem(1))
            self.ui.tblMain.setCurrentCell(row, 3)
        elif column == 3:
            if self.ui.tblMain.item(row, 0) == None:
                self.ui.tblMain.setCurrentCell(row, 0)
                return
            item.setFlags(Qt.ItemIsEditable|Qt.ItemIsEnabled)
            self.ui.tblMain.editItem(item)
        elif column == 4:
            if not self.is_int(self.ui.tblMain.item(row, 3).text()):
                self.ui.tblMain.setItem(row, 3, QTableWidgetItem(1))
                self.ui.tblMain.setCurrentCell(row, 3)
            else:
                total = int(self.ui.tblMain.item(row, 3).text()) * float(self.ui.tblMain.item(row, 2).text()[1:])
                print total
                self.ui.tblMain.setItem(row, 4, QTableWidgetItem('$%1.2f' % total))
                
    def advance(self):
        current_row = self.ui.tblMain.currentRow()
        current_column = self.ui.tblMain.currentColumn()
        if current_column == 4 and current_row == self.ui.tblMain.rowCount() - 2:
            self.ui.tblMain.insertRow(self.ui.tblMain.rowCount() - 1)
            self.ui.tblMain.setCurrentCell(current_row+1, 0)
        else:
            self.ui.tblMain.setCurrentCell(current_row, current_column+1)

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    window = Main() 
    window.show()
    #parts = SelectParts()
    #parts.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
