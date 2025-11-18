from PyQt6 import QtCore, QtGui, QtWidgets
from random import randint
import sys

# pyuic6 помог
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 101, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Нарисовать круг"))


class Widget(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.color = QtGui.QColor(255, 204, 0) # цвет яндекса :)
        self.radius = 0
        self.x, self.y = 0, 0
        self.pushButton.clicked.connect(self.draw_circle)
    
    def draw_circle(self):
        self.radius = randint(10, 50)
        self.x = randint(0, 399)
        self.y = randint(0, 299)
        self.update()
    
    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setBrush(self.color)
        qp.drawEllipse(self.x, self.y, self.radius, self.radius)
        qp.end()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Widget()
    sys.exit(app.exec())
