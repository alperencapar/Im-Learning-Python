import sqlite3

con = sqlite3.connect("kütüphane.db")       #con >>> connection. sqlite3 kütüphanesinin altındaki connect metodunu kullandık
#kütüphane.db adı altında bir dosya varsa, sadece bağlanacak. Yoksa, oluşturup bağlanacak

cursor = con.cursor()                   #veritabanı üzerinde işlem gerçekleştirmek için cursor(imleç) belirliyoruz

def tablo_olustur():
    #cursor.execute =>> çalıştır 
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)")  # Tablo yoksa kitaplık adında tablo oluştur ve şu sütünları ekle
    con.commit()        #sorgunun çalışması için gerekli (Veritabanını GÜNCELLEME istediğimizi belirtiyoruz) 

def veri_ekle():
    cursor.execute("Insert Into kitaplık Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()



def veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("Insert Into kitaplık Values (?,?,?,?)", (isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()

def verileri_al():
    cursor.execute("SELECT * FROM kitaplık")
    liste = cursor.fetchall()     #cursor'un bilgilerini fetchall ile alıp listeye ekliyoruz
    print("Kitaplık tablosunun bilgileri...")
    for i in liste:
        print(i)


def verileri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi = ?",(yayınevi,)) # Sadece yayınevi ,Everest olan kitapları alıyoruz.
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)


def tablo_bilgi_guncelle(eski_yayinevi,yayinevi):
    print("{} Tablodan siliniyor".format(yazar))
    sleep(0.5)
    cursor.execute("UPDATE kitaplık set Yayınevi = ? Where Yayınevi = ?",(yayinevi,eski_yayinevi))  #ilk yeni bilgi sonra eski bilgi
    cursor.execute("Select * FROM kitaplık Where Yayınevi = ? ",(yayinevi,))
    data = cursor.fetchall()
    for i in data:
        print(i)
    con.commit()
    
    
def veri_sil(yazar):
    cursor.execute("DELETE From kitaplık Where Yazar = ?",(yazar,))
    con.commit()
    verileri_al()






tablo_olustur()

# isim = input("Kitap İsim: ")
# yazar = input("Kitap Yazarı: ")
# yayinevi = input("Yayınevi: ")
# sayfa_sayisi = int(input("Sayfa Sayısı: "))

# verileri_al()

#veri_ekle()
# veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi)
# verileri_al3("MediaCat")
# tablo_bilgi_guncelle("Karbon","Türkiye İş Bankası Kültür Yayınları")


veri_sil("Ahmet Ümit")

con.close()     #kapatmamız gerekiyor

