import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_Form

def egcd(e, fn):
	if e == 0:
		return (fn, 0, 1)
	else:
		gcd, d, y = egcd(fn % e, e)
		return (gcd, y - (fn//e) * d, d)

def ecrypto(l1,l2,e,text):
    n = l1*l2
    fn = (l1-1)*(l2-1)
    gcd, d, y = egcd(e, fn)

    C = (text**e)%n
    k=d%fn
    return  C , n , k 




def main():
    #Create application
    app = QtWidgets.QApplication(sys.argv)
 

    #Create Form and UI
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    #Hook logic
    def input():
        try:
            ui.label_7.setText("")
            l1=int(ui.lineEdit.text())
            l2=int(ui.lineEdit_2.text())
            e=int(ui.lineEdit_3.text())
            text=int(ui.textEdit.toPlainText())
            C,n,k = ecrypto(l1,l2,e,text)
            ui.textEdit_3.setText(str(C))
            ui.lineEdit_4.setText(str(n))
            ui.lineEdit_5.setText(str(k))
        except:
            ui.label_7.setText("Дані введено не коректно")

    
    ui.pushButton_3.clicked.connect( input )

    
    #Run main loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()