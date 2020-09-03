import sys

from PyQt5 import QtWidgets,QtGui

def Pencere():

    app = QtWidgets.QApplication(sys.argv)      

    pencere = QtWidgets.QWidget()              

    pencere.setWindowTitle("PyQt5 Ders 2- Pencere içi işlemler")   
    pencere.setGeometry(100,100,500,500)        #ilk iki değer nereden başlayacağını, sonraki iki değer pencere büyüklüğü)x,y,x,y (show'dan önce yazılmalı)
    etiket1 = QtWidgets.QLabel(pencere)         #etiket1 objesini pencere üzerine yerleştiriyoruz
    etiket2 = QtWidgets.QLabel(pencere)

    etiket1.setText("Burası Bir Yazı")
    etiket1.move(220,100)                       #etiket1 adlı yazımızı x,y koordinatında taşıdık    (yatay, dikey)

    etiket2.setPixmap(QtGui.QPixmap("python.png"))  #resim oluştu
    etiket2.move(70,150)


    pencere.show()                              

    sys.exit(app.exec_())       

Pencere()