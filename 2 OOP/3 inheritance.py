from time import sleep
class Calisan():

    def __init__(self,isim,maas,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileriGoster(self):      #init fonksiyonunda nesneler tanımlandığı için diğer fonksiyonlardan erişebiliriz
        print("Çalışan sınıfı bilgileri")

        print("İsim: {}\nMaaş: {}\nDepartman: {}\n\n\n".format(self.isim,self.maas,self.departman))


    def departmanDegistir(self,yeni_departman):
        self.departman = yeni_departman




class Yonetici(Calisan):    #Yonetici sınıfı, Calisan sınıfından özellikleri kalıtım olarak alıyor

    def zamYap(self,zam_miktari):
         self.maas += zam_miktari 


    #overriding 

    def __init__(self,isim,maas,departman,kisi_sayisi):
        print("Yönetici sınıfı init fonksiyonu")
        
        super().__init__(isim,maas,departman)       #self.isim = isim self.maas = maas self.departman = departman yazmakla aynı şey


        #super
        
        self.kisi_sayisi = kisi_sayisi

        #inheritance yaptığımız class'taki fonksiyon adıyla yeni bir fonksiyon tanımlarsak, yeni tanımaldığımız fonksiyon çağrılır
     
    def bilgileriGoster(self):
        print("Bilgiler Yükleniyor...")
        sleep(1)
        print("Bilgiler:\n\n\nİsim: {}\nMaaş: {}\nDepartman:{}\nSorumlu Olduğu Kişi Sayısı:{}\n\n".format(self.isim,self.maas,self.departman,self.kisi_sayisi))
    

class Kitap():
    
    #https://diveintopython3.net/special-method-names.html

    def __init__(self,isim,yazar,sayfa_sayisi,):
        print("init online".title())
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
    
    def __str__(self):          #override
        return ("\n\nstr online \n\n\n\nİsim: {}\nYazar: {}\nSayfa Sayısı: {}\n".format(self.isim,self.yazar,self.sayfa_sayisi))


    def __len__(self):          #override edildi
        return self.sayfa_sayisi    #len() metodu sayfa sayısını döndürecek


    def __del__(self):          #del metodunu override edemiyoruz, üstüne ek özellikler ekleyebiliyoruz
        sleep(1)
        print("Kitap Objesi Siliniyor...")
        sleep(2)
        print("Kitap Objesi Silindi!".upper())


# kitap = Kitap("Beyin","David Eagleman",220)
# print(kitap)        #kitap objesini yazdırıyoruz ve __str__ metodu çalışıyor
# print(len(kitap))

kitap2 = Kitap("İknanın Psikolojisi","Robert B. Cialdini",382)


