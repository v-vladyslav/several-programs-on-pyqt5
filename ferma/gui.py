# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(464, 468)
        Form.setMinimumSize(QtCore.QSize(464, 468))
        Form.setMaximumSize(QtCore.QSize(464, 468))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(39, 38, 38);\n"
"color: white;\n"
"font-family: sans-serif;")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(240, 230, 191, 41))
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setStyleSheet("border-bottom: 2px solid white;\n"
"padding: 10px;")
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 300, 231, 21))
        self.label_3.setMinimumSize(QtCore.QSize(170, 0))
        self.label_3.setStyleSheet("font-family: sans-serif;\n"
"font-size: 18px;")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(40, 340, 389, 87))
        self.textEdit.setStyleSheet("border: 2px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"padding: 5px;")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 130, 131, 41))
        self.pushButton.setStyleSheet("border: 2px solid white;\n"
"border-radius: 10px;\n"
"font-size: 14px;\n"
"font-weight: bold;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 50, 115, 31))
        self.label.setMinimumSize(QtCore.QSize(110, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setStyleSheet("font-family: sans-serif;\n"
"font-size: 18px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 227, 170, 41))
        self.label_2.setMinimumSize(QtCore.QSize(170, 0))
        self.label_2.setMaximumSize(QtCore.QSize(170, 16777215))
        self.label_2.setStyleSheet("font-family: sans-serif;\n"
"font-size: 18px;")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(240, 50, 191, 38))
        self.lineEdit.setStyleSheet("border: none;\n"
"border-bottom: 2px solid white;\n"
"padding: 9px;\n"
"color: white;\n"
"font-size: 14px;\n"
"font-weight: bold;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(140, 170, 171, 20))
        self.label_7.setStyleSheet("color:red;")
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "АТАКА РОЗКЛАД НА МНОЖНИКИ"))
        self.label_3.setText(_translate("Form", "Секретні елементи p та q:"))
        self.pushButton.setText(_translate("Form", "Розкласти"))
        self.label.setText(_translate("Form", "Введіть ключ:"))
        self.label_2.setText(_translate("Form", "Використаний час:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
