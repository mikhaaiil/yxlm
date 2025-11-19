from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 295)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 381, 16))
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 60, 341, 152))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.nameLineEdit)
        self.roastingLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.roastingLabel.setObjectName("roastingLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.roastingLabel)
        self.roastingComboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.roastingComboBox.setObjectName("roastingComboBox")
        self.roastingComboBox.addItem("")
        self.roastingComboBox.addItem("")
        self.roastingComboBox.addItem("")
        self.roastingComboBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.roastingComboBox)
        self.typeLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.typeLabel.setObjectName("typeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.typeLabel)
        self.typeComboBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.typeComboBox.setObjectName("typeComboBox")
        self.typeComboBox.addItem("")
        self.typeComboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.typeComboBox)
        self.tasteLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.tasteLabel.setObjectName("tasteLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.tasteLabel)
        self.tasteLineEdit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.tasteLineEdit.setObjectName("tasteLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tasteLineEdit)
        self.priceLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.priceLabel.setObjectName("priceLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.priceLabel)
        self.priceSpinBox = QtWidgets.QSpinBox(parent=self.formLayoutWidget)
        self.priceSpinBox.setObjectName("priceSpinBox")
        self.priceSpinBox.setRange(0, 10000)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.priceSpinBox)
        self.volumeLabel = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.volumeLabel.setObjectName("volumeLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.volumeLabel)
        self.volumeSpinBox = QtWidgets.QSpinBox(parent=self.formLayoutWidget)
        self.volumeSpinBox.setObjectName("volumeSpinBox")
        self.volumeSpinBox.setRange(0, 1000)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.volumeSpinBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "change/add nformation about the drink:"))
        self.nameLabel.setText(_translate("Dialog", "name"))
        self.roastingLabel.setText(_translate("Dialog", "roasting"))
        self.roastingComboBox.setItemText(0, _translate("Dialog", "Светлая"))
        self.roastingComboBox.setItemText(1, _translate("Dialog", "Средняя"))
        self.roastingComboBox.setItemText(2, _translate("Dialog", "Темная"))
        self.roastingComboBox.setItemText(3, _translate("Dialog", "Очень темная"))
        self.typeLabel.setText(_translate("Dialog", "type"))
        self.typeComboBox.setItemText(0, _translate("Dialog", "В зернах"))
        self.typeComboBox.setItemText(1, _translate("Dialog", "Молотый"))
        self.tasteLabel.setText(_translate("Dialog", "taste"))
        self.priceLabel.setText(_translate("Dialog", "price"))
        self.volumeLabel.setText(_translate("Dialog", "volume"))


class AddEditWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None, mode="add", item=None):
        super().__init__(parent)
        self.setupUi(self)
        if mode == "edit":
            self.set_data(item)
    
    def set_data(self, item: list[QtWidgets.QTableWidgetItem]):
        print(item)
        name, roasting, _type, taste, price, volume = [i.text() for i in item[1:]]
        self.nameLineEdit.setText(name)
        self.roastingComboBox.setCurrentText(roasting)
        self.typeComboBox.setCurrentText(_type)
        self.tasteLineEdit.setText(taste)
        self.priceSpinBox.setValue(int(price))
        self.volumeSpinBox.setValue(int(volume))

    def get_data(self):
        return {
            "name": self.nameLineEdit.text(),
            "roasting": self.roastingComboBox.currentText(),
            "type": self.typeComboBox.currentText(),
            "taste": self.tasteLineEdit.text(),
            "price": int(self.priceSpinBox.value()),
            "volume": int(self.volumeSpinBox.value())
        }
