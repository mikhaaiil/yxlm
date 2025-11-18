from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import sqlite3


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class Widget(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initTable()
    
    def initTable(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        cur.execute("SELECT * FROM coffee")
        lines = cur.fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(len(lines))
        self.tableWidget.setHorizontalHeaderLabels(
            ["id", "name", "roasting", "type", "taste", "price", "volume"]
        )
        for r, row in enumerate(lines):
            for c, val in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(val))
                self.tableWidget.setItem(r, c, item)
        _header = self.tableWidget.horizontalHeader()
        _header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        _header.setStretchLastSection(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec())
