#esnek yapılar
""" 
def fonksyion(*args):   #gönderdiğimiz değerler demet haline geliyor
    for i in args:      #for döngüsü ile içinde geziniyoruz
        print(i)

 """
# fonksyion(1,2,3,4,5,6,7,8)

""" 

def fonks(isim,*args):
    print("isim",isim)

    for i in args:
        print(i)

     """
# fonks("Alp",1,2,3,4,5)


""" 
def fonk(**kwargs):     #dict halinde yani değişkene isim vererek atayabiliyoruz
    # print(kwargs)
    for i,j in kwargs.items():
        print("Argüman ismi: ",i,"Argüman değeri: ",j)
 """
# fonk(isim = "Murat", soyisim = "Murat")


""" 
def fonksiyon_mix(*args,**kwargs):
    for i in args:
        print("Argümanlar:",i)
    print("------------------------------")
    for i ,j in kwargs.items():
        print("Argüman İsmi:",i,"Argüman Değeri:",j)

 """

# fonksiyon_mix(1,2,3,4,5,6,7,isim = "Alp",soyisim = "Eren", numara = 12345)


#fonksiyon aktarma

def selamla(isim):
    print("Selam",isim)


merhaba = selamla       #selamla fonksiyonu merhaba'ya aktarıldı

# merhaba("ece")

# del selamla
# print(selamla)  #silindi
# print(merhaba)    #silinmemiş




#iç içe fonksiyon tanımlama

""" 
def fonksiyon_bir():


    def fonksiyon_iki():
        print("Küçük fonksiyon çalıştı")

    fonksiyon_iki()
    print("Büyük fonksiyon çalıştı")

fonksiyon_bir()
 """

""" 
def fonksiyon(*args):

    def toplama(args):

        toplam = 0
        for i in args:
            toplam += i
        return toplam
    print(toplama(args))    # iç fonksiyon çalışıyor

fonksiyon(1,2,3,4,5,6,7,8,9)
 """

""" 
def mainfonksiyon(islem):


    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam


    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim

    if islem == "toplama":
        return toplama
    else:
        return carpma



deneme = mainfonksiyon("toplama")

print(deneme)                       #deneme, toplama fonksiyonuna eşitlendi

print(deneme(1,2,3,4,5,6,7,8,9))

deneme2 = mainfonksiyon("carpma")   #deneme, carpma fonksiyonuna eşitlendi

print(deneme2(1,2,3,4,5))
 """


""" 

def toplama(a,b):
    return a + b
def çıkarma(a,b):
    return a-b
def çarpma(a,b):
    return a * b
def bölme(a,b):
    return a / b



def anafonksiyon(func1,func2,func3,func4,işlem_adı): # Tanımladığımız 4 fonksiyonu da argüman olarak göndereceğiz.
    if (işlem_adı == "toplama"):
        print(func1(3,4))
    elif (işlem_adı == "çıkarma"):
        print(func2(10,3))
    elif (işlem_adı == "çarpma"):
        print(func3(10,3))
    elif (işlem_adı == "bölme"):
        print(func4(10,4))
    else:
        print("Geçersiz işlem adı...")





anafonksiyon(toplama,çıkarma,çarpma,bölme,"toplama")

 """







                                #Decorator Fonksiyonlar!!!!!!!!!!!!!!!!!!!


""" 
import time

def zaman_hesapla(fonksiyon):
    def wrapper(sayilistesi):       #gelen değeri istediğimiz gibi değerlendiriyoruz
        baslama = time.time()

        sonuc = fonksiyon(sayilistesi)      #gelen fonksiyonu belirtmemiz gerekiyor

        bitis = time.time()
        print(fonksiyon.__name__ + " " + str(bitis-baslama) + " Saniye")
        return sonuc
    return wrapper


@zaman_hesapla
def kare_hesapla(sayilar):
    sonuc = list()
    for i in sayilar:
        sonuc.append(i ** 2)

    return sonuc


@zaman_hesapla
def kup_hesapla(sayilar):
    sonuc = list()

    for i in sayilar:
        sonuc.append(i ** 3)
    print(sonuc)


kare_hesapla(range(10000000))
kup_hesapla(range(10000000))
 
 """

# https://www.youtube.com/watch?v=AjwH2T70xT0



""" 
import time


def zaman_hesapla(fonksiyon):
    def wrapper(a,b):
        baslangic = time.time()

        fonksiyon(a,b)

        bitis = time.time()
        zaman = str(bitis - baslangic)
        print("{} sürede tamamlandı".format(zaman))

    return wrapper


@zaman_hesapla
def topla(x,y):
    print(x + y)


topla(3,5)

 """



