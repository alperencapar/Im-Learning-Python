
from random import randint
from time import sleep


giris = "***************************************\n\nSayı tahmin oyununa hoşgeldin\n\n1 ile 40 arasında rastgele sayı seçilecek ve sizin bu sayıyı bulmanız gerekiyor\n\n***************************************"

print(giris.title())

random_sayi = randint(1,40)

while True:
        giris_hakki = 7
        kullanici_tahmin = int(input("Lütfen bir sayı giriniz: "))

        if(random_sayi > kullanici_tahmin):
                print("Hesaplanıyor...\n\n")
                sleep(1)
                giris_hakki -= 1
                print("Daha Büyük Sayı Giriniz\n\n\n\n")
        elif (random_sayi < kullanici_tahmin):
                print("Hesaplanıyor...\n\n")
                giris_hakki -= 1
                sleep(1)
                print("Daha Küçük Sayı Giriniz\n\n\n\n")
        else:
                print("Hesaplanıyor...\n\n")
                sleep(1)
                print("Tebrikler, Sayıyı Buldunuz!")
                sleep(1)
                print("\n\n\n")
                break
        if (giris_hakki == 0):
                print("Giris hakkınız bitti\n")
                sleep(1)
                print("Oyun kapatılıyor...")
                sleep(1)
                break