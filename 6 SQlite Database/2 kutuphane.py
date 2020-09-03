import sqlite3
class Kitap():

    def __init__(self,isim,yazar,yayinevi,tur,baski):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski


    def __str__(self):
        return "Kitap ismi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBaskı: {}\n".format(self.isim,self.yazar,self.yayinevi,self.tür,self.baskı)


class Kütüphane():

    def __init__(self):
        self.baglanti_olustur()



    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("kütüphane2.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If Not Exists kitaplar (isim Text, yazar Text, yayınevi Text, tür Text, baskı Int)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglanti_kes(self):
        self.baglanti.close()


    def kitaplari_goster(self):
        sorgu = "Select * From kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        if(len(kitaplar) == 0):
            print("Kütüphanede kitap bulunmuyor...")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)    #str fonksiyonu çalışıyor


    def kitap_sorgula(self,isim):
        sorgu = "Select * From kitaplar Where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()
        if (len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor")
        
        else: 
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])   #demet geldiği için iki değişken
            print(kitap)    #yukarıdaki dönen değerleri str üzerinden yazdırıyoruz


    def kitap_ekle(self,kitap):
        sorgu = "Insert Into kitaplar Values(?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski))
        self.baglanti.commit()


    def kitap_sil(self,isim):
        sorgu = "Delete From kitaplar Where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()


    def baski_yukselt(self,isim):
        sorgu = "Select * From kitaplar Where isim = ?"
        self.cursor.execute(sorgu, (isim,))


        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Kitap bulunmuyor")
        else:
            baski = kitaplar[0,4]
            baski += 1
            sorgu2 = "Update kitaplar Set baskı = ? where isim = ?"
            self.cursor.execute(sorgu, (baski,isim))
            self.baglanti.commit()






