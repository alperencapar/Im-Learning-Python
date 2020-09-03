import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QRadioButton, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,QFileDialog
from PyQt5.QtWidgets import QAction,qApp,QMainWindow


class Notepad(QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yazi_alani = QTextEdit()

        self.temizle = QPushButton("Temizle")
        self.ac = QPushButton("Aç")
        self.kaydet = QPushButton("Kaydet")

        h_box = QHBoxLayout()

        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box = QVBoxLayout()

        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)


        self.setLayout(v_box)
        self.setWindowTitle("Notepadd A++")

        self.temizle.clicked.connect(self.yazi_temizle)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)




    def yazi_temizle(self):
        self.yazi_alani.clear()



    def dosya_ac(self):


        #dosya seçmeden kapattığımızda hata döndüğü için try-except blokları arasına yazıldı

        try:
            dosya_isim = QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("Desktop"))         #QWidget,"Pencere ismi",os.getenv("Dizin Parametresi")

            with open(dosya_isim[0],"r") as file:
                self.yazi_alani.setText(file.read())
        except FileNotFoundError:
            pass



    def dosya_kaydet(self):
        dosya_isim = QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("Desktop"))

        with open(dosya_isim[0],"w") as file:
            file.write(self.yazi_alani.toPlainText())      




class Menu(QMainWindow):
    def __init__(self):
        super().__init__()


        self.pencere = Notepad()    #Notepad penceresinden obje oluşturuldu <<<<<<<<<<<<<<>>>>>>>>>>>>>>

        self.setCentralWidget(self.pencere)     #ana pencerenin ortasına pencere ekledik ve Notepad penceresini gönderdik

        self.setWindowTitle("Metin Editörü")

        self.show()

        self.menuleri_olustur()


    def menuleri_olustur(self):
        
        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")

        dosya_ac = QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")

        temizle = QAction("Dosya Temizle",self)
        temizle.setShortcut("Ctrl+D")

        cikis = QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)


        dosya.triggered.connect(self.response)


        self.show()

    def response(self,action):
        if action.text() == "Dosya Aç":
            self.pencere.dosya_ac()

        elif action.text() == "Dosya Kaydet":
            self.pencere.dosya_kaydet()

        elif action.text() == "Dosya Temizle":
            self.pencere.yazi_temizle()

        elif action.text() == "Çıkış":
            qApp.quit()


app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())