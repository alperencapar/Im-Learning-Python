import sys

from PyQt5 import QtWidgets,QtGui

def Pencere():

    app = QtWidgets.QApplication(sys.argv)      
    pencere = QtWidgets.QWidget()          



    #
    buton = QtWidgets.QPushButton(pencere)  #pencereye buton ekle   (pencere oluşturduktan sonra yapılmalı)
    #

    buton.setText("TIKLA")
    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("Merhaba Dünya")
    etiket.move(200,30)
    buton.move(200,80)

    pencere.setWindowTitle("PyQt5 Ders 2 - Buton oluşturma")   
    pencere.setGeometry(100,100,500,500)        



    pencere.show()                              

    sys.exit(app.exec_())       

Pencere()