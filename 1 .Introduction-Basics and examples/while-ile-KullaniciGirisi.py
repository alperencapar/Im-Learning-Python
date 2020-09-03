#while döngüsü ile kullanıcı girişi örneği


sys_kulanici_adi = "alp"
sys_parola = "12345"

giris_hakki = 3
while True:
    kullanici_adi = input("Kullanıcı adı: ")
    parola = input("Parola: ")

    if (kullanici_adi != sys_kulanici_adi and parola == sys_parola):
        print("Kullanıcı adı hatalı!")
        giris_hakki -= 1
    elif (kullanici_adi == sys_kulanici_adi and parola != sys_parola):
        print("Parola yanlış!")
        giris_hakki -= 1
    elif (kullanici_adi != sys_kulanici_adi and parola != sys_parola):
        print("Kullanıcı adı ve Parola yanlış!")
        giris_hakki -= 1
    else:
        print("Giriş yapıldı...")
        break
    if(giris_hakki ==0 ):
        print("Giriş hakkınız kalmadı!")
        break
