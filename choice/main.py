import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_Form

def egcd(v, w): #теорема Евкліда, знаходження мультиплікативної інверсії
        if v == 0:
            return (w, 0, 1)
        else:
            gcd, x, y = egcd(w % v, v)
            return (gcd, y - (w//v) * x, x)





def main():
    #Create application
    app = QtWidgets.QApplication(sys.argv)
 

    #Create Form and UI
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    #Hook logic
    def y():
        try:
            ui.label_3.setText("")
            ui.label_14.setText("")
            ui.label_15.setText("")
            e=int(ui.lineEdit.text())
            n=int(ui.lineEdit_2.text())
            x=int(ui.lineEdit_4.text())
            C=int(ui.textEdit.toPlainText())
            y = (C*(x**e))%n
            ui.lineEdit_3.setText(str(y))
        except:
            ui.label_3.setText("Дані введено не коректно")


    def fun2():
        try:
            ui.label_3.setText("")
            ui.label_14.setText("")
            ui.label_15.setText("")
            n=int(ui.lineEdit_2.text())
            d=int(ui.lineEdit_5.text())
            y=int(ui.lineEdit_3.text())
            z = (y**d)%n
            ui.textEdit_4.setText(str(z))
        except:
            ui.label_14.setText("Дані введено не коректно")
    

    def decrypt():
        try:
            ui.label_3.setText("")
            ui.label_14.setText("")
            ui.label_15.setText("")
            z=int(ui.textEdit_3.toPlainText())
            n=int(ui.lineEdit_2.text())
            y=int(ui.lineEdit_3.text())
            x=int(ui.lineEdit_4.text())
            gcd, xx, y = egcd(x, n)
            M = (z*xx)%n  
            ui.textEdit_2.setText(str(M))
        except:
            ui.label_15.setText("Дані введено не коректно")
    
        
    ui.pushButton_2.clicked.connect( y )
    ui.pushButton_3.clicked.connect( fun2 )
    ui.pushButton.clicked.connect( decrypt )


    
    #Run main loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()