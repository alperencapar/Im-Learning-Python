import sys
from PyQt5 import QtWidgets
import sqlite3


class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.baglanti_olustur()

        self.init_ui()


    def baglanti_olustur(self):
        baglanti = sqlite3.connect("database.db")       #database'e bağlanılıyor
        self.cursor = baglanti.cursor()                 #database cursor oluşturuldu

        self.cursor.execute("Create Table If not exists üyeler (kullanici_adi TEXT, parola TEXT)")  #tablo yok ise oluşturuluyor
        baglanti.commit()



    def init_ui(self):
        self.kullanici_adi = QtWidgets.QLineEdit()                  #input alanı
        self.parola = QtWidgets.QLineEdit()                         #input alanı
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)       #karakterlerin görünmemesini sağlıyor
        self.giris = QtWidgets.QPushButton("Giriş Yap")             #buton
        self.yazi_alani = QtWidgets.QLabel("")


        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)


        h_box = QtWidgets.QHBoxLayout()


        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Kullanıcı Girişi")


        #Butonlara fonksiyon ekleme

        self.giris.clicked.connect(self.login)                  #butona tıklanınca çalıştırılacak fonksiyonu tanıtıyoruz



        self.show() #yazılmaz ise yapılan işlemler gözükmez!

    def login(self):
        adi = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("Select * From üyeler Where kullanici_adi = ? and parola = ?",(adi,par))    #kullanıcı adı ve parola veritabanında sorgulanıyor

        #gelen sorguyu kontrol ediyoruz
        data = self.cursor.fetchall()
        if len(data) == 0:
            self.yazi_alani.setText("Kullanıcı bulunamadı!")
        
        else:
            self.yazi_alani.setText("Hoşgeldin " + adi)


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())

