import sqlite3

class Şarkı():

    def __init__(self,isim,sanatci,suresi):
        self.isim = isim
        self.sanatci = sanatci
        self.suresi = suresi

    def __str__(self):
        return "Şarkı ismi: {}\nYazar: {}\nSanatçı: {}\Süre:".format(self.isim,self.sanatci,self.suresi)

class Liste():


    def __init__(self):
        self.tablo_olustur()

    
    def tablo_olustur(self):
        self.con = sqlite3.connect("Şarkı.db")
        self.cursor = self.con.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS Sarki (İsim TEXT,Sanatçı TEXT, Süre Decimal)"
        self.cursor.execute(sorgu)
        self.con.commit()

    def veri_ekle(self,sarki):
        sorgu = "Insert Into Sarki Values (?,?,?)"
        self.cursor.execute(sorgu,(sarki.isim,sarki.sanatci,sarki.suresi))
        self.con.commit()

    def sure_hesapla(self):
        sorgu = "SELECT Süre FROM Sarki"
        self.cursor.execute(sorgu)
        sure = self.cursor.fetchall()
        
        toplam_sure = 0
        for i in sure:
            toplam_sure += i
        print("Toplam süre: ",toplam_sure)


    def yazdirma(self):
        sorgu = "SELECT * FROM Sarki"
        self.cursor.execute(sorgu)
        sarki = self.cursor.fetchall()
        for i in sarki:
            sarki = Şarkı(i[0],i[1],i[2])
            print (sarki)



liste = Liste()

print("""*****************************
    İşlem seç:
    1.Veri ekle
    2.Sure Hesapla
    3.Yazdır
    
    
    ************************""")

while True:
    secim = input("Seçim yapın: ")
    if(secim == "1"):
        isim = input("Şarkı adı: ")
        sanatci = input("Sanatçı adı: ")
        suresi = int(input("Süresi: "))
        sarki = Şarkı(isim,sanatci,suresi)
        liste.veri_ekle(sarki)

    elif(secim == "2"):
        liste.sure_hesapla()
    elif(secim == "3"):
        liste.yazdirma()