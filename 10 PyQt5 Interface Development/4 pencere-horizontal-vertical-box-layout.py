import sys

from PyQt5 import QtWidgets,QtGui

def Pencere():

    app = QtWidgets.QApplication(sys.argv)      
    okay = QtWidgets.QPushButton("Tamam")       #pencereyi girmemiz gerekmiyor
    cancel = QtWidgets.QPushButton("İptal")



    #yatayda 

    h_box = QtWidgets.QHBoxLayout()     #horizontal box ekleniyor
    h_box.addWidget(okay)               #h_box'un içine okay butonu ekleniyor
    h_box.addStretch()                  #sol ve sağa sabitlendi, boyut değişse bile yerlerinden oynamıyorlar
    h_box.addWidget(cancel)    
    #butonlardan sonra yazınca sola sabitledi. Butonlardan önce yazarsak sağa sabitliyor



    #dikeyde

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()                  #addStrech() metodunu yazdığımız yere göre konum değişiklik göstermektedir
    v_box.addWidget(okay)
    v_box.addWidget(cancel)
    




    v_box.addLayout(h_box)          #v_box'un içerisine h_box'u ekledik. Daha önceden eklenen Strech'ler (margin) sayesinde butonlar en alta sabitlendi  

    pencere = QtWidgets.QWidget()      

    #pencere.setLayout(h_box)            #pencereye h_box ekleniyor
    pencere.setLayout(v_box)  


    pencere.setWindowTitle("PyQt5 Ders 2 - Buton oluşturma")   
    pencere.setGeometry(100,100,500,500)        



    pencere.show()                              
    sys.exit(app.exec_())       

Pencere()