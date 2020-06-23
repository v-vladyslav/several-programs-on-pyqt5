import sys
import math
import time 
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import  Ui_Form

def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n) 
    return Ans  

def main():
    #Create application
    app = QtWidgets.QApplication(sys.argv)

    #Create Form and UI
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    #Hook logic
    def bp():
        start_time = time.time()
        try :
            ui.label_7.setText("")   
            x=ui.lineEdit.text()
            n=Factor(int(x))        
            ui.textEdit.setText(str(n))
            ui.label_6.setText(str(time.time() - start_time))
        except :
            ui.label_7.setText("Дані введено не коректно")    

            
       

    ui.pushButton.clicked.connect( bp )
    


    #Run main loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
   


