import random 
import time

class Kumanda():


    def __init__(self,tv_durum ="Kapalı",tv_ses = 0,kanal_listesi =["Trt"],kanal = "Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):
        if(self.tv_durum == "Açık"):
            print("Televizyon zaten açık")

        else:
            print("Televizyon Açılıyor....")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if(self.tv_durum == "Kapalı"):
            print("Televizyon zaten kapalı")

        else:
            print("Televizyon kapatılıyor...")
            self.tv_durum = "Kapalı"

    def ses_azalt_arttir(self):

        while True:
            ses_islem = input("Arttırmak için: +\nAzaltmak için: - \nÇıkmak için: q tuşuna basınız: ")
            if(ses_islem =="-"):
                if(self.tv_ses != 0 ):
                    self.tv_ses -= 1
                    print("\n\nSes Seviyesi: ",self.tv_ses)
            elif(ses_islem =="+"):
                if(self.tv_ses != 32):
                    self.tv_ses += 1
                    print("\n\nSes Seviyesi: ",self.tv_ses)
            else:
                break



    def __str__(self):      #kumanda objesini direk yazdırınca çalışacak
        print("\nTV Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\n Şuanki Kanal: {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal))

    def __len__(self):       #kanal listesi uzunluğu yazılıyor
        return len(self.kanal_listesi)

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi)-1 )

        self.kanal = self.kanal_listesi[rastgele]
        print("Kanal {} olarak değiştirldi",self.kanal)

    def kanal_ekle(self,kanal):
        print("Kanal ekleniyor...")
        self.kanal_listesi.append(kanal)
        time.sleep(0.2)
        print("Kanal eklendi: ",kanal)

    def ses_mute(self):
        if(self.tv_ses != 0):
            global ses_seviye
            ses_seviye = self.tv_ses

        if(self.tv_ses > 0):
            self.tv_ses = 0
            print("ses seviyesi: ",self.tv_ses)

        elif(self.tv_ses == 0):
            self.tv_ses = ses_seviye 
            print("ses seviyesi: ",self.tv_ses)
                
    # def ses_seviye_return(self):
    #     return self.tv_ses
    
kumanda = Kumanda()

print("""*******************

Televizyon Uygulaması

İşlemler:

1. Televizyonu Aç

2. Televizyonu Kapat

3. Televizyon Bilgileri

4. Kanal Sayısını Öğrenme

5. Kanal Ekle

6. Rastgele Kanal'a Geç

7. Sesi Azalt Ya da Artır

8. Sesi Tamamen Kapat,Aç

Çıkmak için 'q' ya basın.

*******************""")

while True:
    islem = input("İşlem seçiniz: ")

    if(islem =="q"):
        break
    elif(islem == "1"):
        kumanda.tv_ac()
    elif(islem == "2"):
        kumanda.tv_kapat()
    elif(islem == "3"):
        print(kumanda)  #str metodu çalışıyor
    elif(islem == "4"):
        print("Kanal sayısı: ",len(kumanda))    #len metodu çalışıyor
    elif(islem == "5"):
        kanallar = input("Eklemek istediğiniz kanalları ',' ile ayırın! ")
        eklenecekler.kanallar.split(",")
        for i in eklenecekler:
            kumanda.kanal_ekle(i)
        print("Kanal listesi güncellendi")
    elif(islem == "6"):
        kumanda.rastgele_kanal()
    elif(islem == "7"):
        kumanda.ses_azalt_arttir()
    elif(islem =="8"):
        kumanda.ses_mute()

    else:
        print("Geçersiz işlem!")
    

    

    