from time import sleep

class Yazilimci():

    def __init__(self,isim,soyisim,numara,diller,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.diller = diller
        self.maas = maas


    def bilgileriGoster(self):
        print(""" Yazılımcı objesinin özellikleri:
        İsim: {}
        Soyisim: {}
        Numara: {}
        Bildiği Yazılım Dilleri: {}
        Maaş: {}""".format(self.isim,self.soyisim,self.numara,self.diller,self.maas))
    def zamYap(self,zam_miktari):
        print("{}₺ Zam yapılıyor".format(zam_miktari))
        sleep(1)
        self.maas += zam_miktari
        print("Başarı ile zam yapıldı. Toplam maaş: {}".format(self.maas))



yazilimci = Yazilimci("Alp","Çapar",14558971485,["Python","Java","JS"],3500)

yazilimci.bilgileriGoster()

yazilimci.zamYap(200)
yazilimci.bilgileriGoster()