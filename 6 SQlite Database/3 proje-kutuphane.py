from kutuphane import *

print("""**********************************
Kütüphane Programı Online

1. Kitapları Göster
2. Kitap Sorgulama
3. Kitap Ekle
4. Kitap Sil
5. Baskı Sayısı Yükselt


Çıkmak için 'q' tuşuna basın


*****************************************""")


kütüphane = Kütüphane()

while True:
    islem = input("İşlem Seçin: ")
    if (islem == "q"):
        print("İşlem sonlandırılıyor")
        break

    elif(islem == '1'):
        kütüphane.kitaplari_goster()
    elif(islem == '2'):
        isim = input("Kitap İsmini giriniz: ")
        kütüphane.kitap_sorgula(isim)
    elif(islem == '3'):
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayinevi = input("Yayınevi: ")
        tur = input("Tür: ")
        baski = int(input("Baskı: "))

        yeni_kitap = Kitap(isim,yazar,yayinevi,tur,baski)
        print("Kitap ekleniyor")
        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi")

    elif(islem == '4'):
         isim = input("Hangi kitabı silmek istyorsunuz ? İsim: ")
         kütüphane.kitap_sil(isim)
    elif(islem == '5'):
        isim = input("Hangi kitabı baskısını yükseltmek istyorsunuz ? İsim: ")
        kütüphane.baski_yukselt(isim)
        print("Baskı yükseltildi")

    else:
        print("Geçersiz İşlem")