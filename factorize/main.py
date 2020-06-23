import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_Form

def First_funk(firs,second):# Функція (p-1)*(q-1)
    fn = (firs - 1) * (second - 1)
    return fn

def egcd(e, fn):
	if e == 0:
		return (fn, 0, 1)
	else:
		gcd, d, y = egcd(fn % e, e)
		return (gcd, y - (fn//e) * d, d)

def output(z,e):
    a ,b,c= [],[],[]


    if z > 5:
        for i in range(1, z+1):
            if(z%i==0):
                a.append(i)

    a = a[1:(len(a)-1)]#Обрізання списку
    a.reverse()

    for i in a:
        c.append(i)
    a.reverse()
    buf = 0
    for i in range(int(len(a)/2)):
        b.append([a[buf],c[buf]])
        buf+=1
    l1=str(b)
    #ui.textEdit.setText(str(b))#Пари простих множників

    
    a.clear()
    buf = 0
    for i in range(int(len(b))):
        a.append(First_funk(b[buf][0],b[buf][1]))
        buf+=1
    l2=str(a)
    #ui.textEdit_2.setText(str(a))#ф(n) утворена парама простих множників


    v = e
    w = a
    buf1 = []
    buf = 0
    for i in w:
        gcd, x, y = egcd(v, w[buf])
        buf+=1
        buf1.append(x)
    buf = 0
    k=[]
    for i in w:
        d = buf1[buf]%i
        k.append(d)
        buf= buf + 1
    l3=str(k)
    #ui.textEdit_3.setText(str(k))#Можливий секретний ключ:
    return l1,l2,l3



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
            ui.label_6.setText("")
            z=int(ui.lineEdit.text())
            e=int(ui.lineEdit_2.text())
            l1,l2,l3 = output(z,e)
            ui.textEdit.setText(l1)
            ui.textEdit_2.setText(l2)
            ui.textEdit_3.setText(l3)
        except:
            ui.label_6.setText("Дані введено не коректно")




    ui.pushButton.clicked.connect(input)


    
    #Run main loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()