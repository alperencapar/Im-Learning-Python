import sys
from PyQt5 import QtWidgets,QtGui


class Pencere(QtWidgets.QWidget):       #kalıtım

    def __init__(self):

        super().__init__()      #normal pencere olarak kullanmak için QWidget özelliklerini tanımlamamız lazım. Miras aldığımız init fonksiyonunu kullanıyoruz
        #QWidget çalıştırıldı

        self.init_ui()

    def init_ui(self):
        self.yazi_alani = QtWidgets.QLabel("Henüz tıklanmadı")
        self.buton = QtWidgets.QPushButton("Bana Tıkla")
        self.say = 0

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)       #self pencere objesini ifade ediyor

        self.buton.clicked.connect(self.click)      #butona tıkladığımızda self.click fonksiyonu çalışacak. Yani fonksiyona bağlama yapıldı

        self.show()

    def click(self):
        self.say += 1
        self.yazi_alani.setText("{} Defa Tıklandı".format(self.say))


app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())







   