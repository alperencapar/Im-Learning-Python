import sys
from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow   
#QAction (menüler içerisinde aksiyon oluşturmak için kullanılıyor)
#qApp  (uygulamadan çıkış yapmak için kullanılıyor)
#QMainWindow (ana pencere)

class Menu(QMainWindow):

    def __init__(self):
        super().__init__()

        menubar = self.menuBar()        #üst bardaki "file,edit,selection" kısmını temsil ediyor

        dosya = menubar.addMenu("Dosya")        #üst bara "Dosya" adında menu çubuğu eklendi
        duzenle = menubar.addMenu("Düzenle")    #üst bara "Düzenle" adında menu çubuğu eklendi

        dosya_ac = QAction("Dosya Aç",self)     #"Dosya Aç" adında bir aksiyon oluşturuldu
        dosya_ac.setShortcut("Ctrl+O")          #"Dosya Aç" aksiyonuna kısayol eklendi, artık kısayol ile erişilebilir

        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")

        cikis = QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+X")


        dosya.addAction(dosya_ac)               #"Dosya" menüsünün altına "dosya_ac" eklendi
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)


        #menünün altına menü ekleme

        bul_ve_degistir = duzenle.addMenu("Bul ve Değiştir")        #düzenle menüsünün altına bul ve değiştir >>>menüsü<<< eklendi
        ara = QAction("Ara",self)
        degistir = QAction("Değiştir",self)

        bul_ve_degistir.addAction(ara)
        bul_ve_degistir.addAction(degistir)

        temizle = QAction("Temizle",self)
        duzenle.addAction(temizle)                                  #menü olmayan aksiyon eklendi!



        #Aciton'lara işlev verme

        cikis.triggered.connect(self.cikis_yap)
        

        #hangi aciton'a basıldığını tespit etme

        dosya.triggered.connect(self.response)      #dosya menüsü altında herhangi bir action tetiklendiği zaman response fonksiyonu çalışsın



        self.setWindowTitle("Menüler")
        self.show()


    def cikis_yap(self):
        qApp.quit()

    def response(self,action):          #python otomatik olarak içerisine action objesi gönderiyor
        
        if action.text() == "Dosya Aç":
            print("Dosya Aç'a basıldı")
        elif action.text() == "Dosya Kaydet":
            print("Dosya Kaydet'e basıldı")
        elif action.text() == "Çıkış":
            print("Çıkış'a basıldı")
    




app = QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())