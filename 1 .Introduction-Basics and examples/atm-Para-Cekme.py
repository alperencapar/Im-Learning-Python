#ATM PROGRAMI

islemler = "Bakiye Sorgulama: 1\nPara Yatırma: 2\nPara Çekme: 3\nÇıkmak için q tuşuna basın..."
print(islemler)

bakiye = 1000

while True:
    islem = input("İşlem Seçiniz: ")

    if(islem == "q"):
        print("Çıkış yapılıyor...")
        break
    
    elif (islem == "1"):
        print("Bakiyeniz {} ₺'dir".format(bakiye))

    elif (islem == "2"):
        yatirilacak_miktar = int(input("Yatırılacak miktarı giriniz: "))
        if(yatirilacak_miktar > 0 ):
            bakiye += yatirilacak_miktar
        elif(yatirilacak_miktar < 0):
            print("Geçersiz miktar!")
        elif(yatirilacak_miktar == 0):
            print("0₺ yatıramazsınız!!!")
    elif (islem == "3"):
        cekilecek_miktar = int(input("Çekilecek miktarı giriniz: "))
        if (cekilecek_miktar > bakiye):
            print("Bakiyeniz yetersiz")
            continue
        else:
            print("Para çekme işlemi başlıyor...")
            bakiye -= cekilecek_miktar
            print("İşlem başarılı.\nKalan bakiyeniz {}₺".format(bakiye))

    else:
        print("geçersiz işlem!")