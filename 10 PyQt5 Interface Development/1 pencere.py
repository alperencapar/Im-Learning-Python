import sys

from PyQt5 import QtWidgets

def Pencere():

    app = QtWidgets.QApplication(sys.argv)      #uygulma objesi oluşturduk ve (komut satırından göndereceğimiz argümanı fonksiyona gönderdik)

    pencere = QtWidgets.QWidget()              #pencere oluşturuldu

    pencere.setWindowTitle("PyQt5 Ders 1")      #pencereye başlık eklendi

    pencere.show()                              #pencere gösterildi

    sys.exit(app.exec_())       #kapatma tuşuna basmadığımız sürece pencereyi çalıştırıyor

Pencere()       #pencere çalıştırılıyor