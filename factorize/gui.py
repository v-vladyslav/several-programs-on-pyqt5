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
        Form.resize(788, 691)
        Form.setMinimumSize(QtCore.QSize(788, 691))
        Form.setMaximumSize(QtCore.QSize(788, 691))
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet("background-color: rgb(39, 38, 38);\n"
"color: white;\n"
"font-family: sans-serif;")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(220, 510, 351, 141))
        self.textEdit.setStyleSheet("border: 2px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"padding: 5px;")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(220, 470, 231, 21))
        self.label_3.setMinimumSize(QtCore.QSize(165, 0))
        self.label_3.setBaseSize(QtCore.QSize(0, 165))
        self.label_3.setStyleSheet("font-family: sans-serif;\n"
"font-size: 18px;")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(410, 270, 351, 161))
        self.textEdit_2.setStyleSheet("border: 2px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"padding: 5px;")
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(410, 230, 361, 21))
        self.label_4.setStyleSheet("font-family: sans-serif;\n"
"font-size: 18px;")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.textEdit_3 = QtWidgets.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(30, 270, 351, 161))
        self.textEdit_3.setStyleSheet("border: 2px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"padding: 5px;")
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 230, 241, 21))
        self.label_5.setBaseSize(QtCore.QSize(1200, 0))
        self.label_5.setStyleSheet("font-family: sans-serif;\n"
"font-size: 18px;")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 130, 151, 41))
        self.pushButton.setStyleSheet("border: 2px solid white;\n"
"border-radius: 10px;\n"
"font-size: 14px;\n"
"font-weight: bold;")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(520, 50, 237, 41))
        self.lineEdit_2.setStyleSheet("border: none;\n"
"border-bottom: 2px solid white;\n"
"padding: 9px;\n"
"color: white;\n"
"font-size: 14px;\n"
"font-weight: bold;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(420, 50, 91, 41))
        self.label_2.setStyleSheet("font-family: sans-serif;\n"
"font-size: 18px;")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 237, 41))
        self.lineEdit.setStyleSheet("border: none;\n"
"border-bottom: 2px solid white;\n"
"padding: 9px;\n"
"color: white;\n"
"font-size: 14px;\n"
"font-weight: bold;")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 50, 91, 41))
        self.label.setStyleSheet("font-family: sans-serif;\n"
"font-size: 18px;")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(320, 180, 151, 16))
        self.label_6.setStyleSheet("color:red;")
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "АТАКА ФАКТОРІЗАЦІЇ"))
        self.label_3.setText(_translate("Form", "Пари простих множників:"))
        self.label_4.setText(_translate("Form", "ф(n) утворена парама простих множників:"))
        self.label_5.setText(_translate("Form", "Можливий секретний ключ:"))
        self.pushButton.setText(_translate("Form", "Знайти"))
        self.label_2.setText(_translate("Form", "Введіть e:"))
        self.label.setText(_translate("Form", "Введіть n:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
