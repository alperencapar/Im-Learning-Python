# I have collected all python codes that i write while i've learning Python. Description lines and variable names are Turkish

""" 

print ("Hello World")
print("----------")


hello = "Hello World"

print (hello)


sayi = 10
print(sayi)
print("\n")

ondalikli_sayi = 3.14
print(ondalikli_sayi)
print("\n")

yazi = "string"
print(yazi)
print("\n")

a = 4
b = 2
c = a + b
print(c)
print("\n")

pi_sayisi = 3.14
cap = 4
cevre = pi_sayisi * cap

#  iki şekilde yazılabilir

print("Çapı 4 olan dairenin çevresi: ", cevre) 
print("Çapı 4 olan dairenin çevresi: {0} ".format(cevre)) ######formatlama {0,1 olarak da kullanılabilir}
print("\n")


# değişkenlerin değerlerini değiştirme (swap)
x = 2
y = 3
print("x:",x, "y:",y)
print("Değiştirme işlemi yapılıyor...")
x,y=y,x
print("işlem tamamlandı")
print("x:",x, "y:",y)
print("\n")

 """

#####################       Tür dönüşümleri     ##################

""" 
a = 47

a = float(a)        #int to float
print(a)

a = int(a)
print(a)

pi = 3.14
pi = int(pi)        #float to int
print(pi)


bum = str(123)      #int to string
print(type(bum))


yazi = "1234455"
yazi = int(yazi)    #str to int
print(yazi, type(yazi))

alinyazisi = "4.414"
alinyazisi = float(alinyazisi)    #str to float
print(alinyazisi, type(alinyazisi))

 """



                                                                                ############### Liste Veri Tipi
""" 
liste = [1,2,3,4,5,"muz",3.14]                          #Listelerde aynı anda farklı veri tipinde veri saklayabilirsin
print(type(liste),liste);


liste2 = list()                                         #boş liste oluşturma
print(liste2)

print("liste uzunluğu: ",len(liste),"\n")               #len uzunluğu veriyor

liste = list("MerhabalarAQ")                            #her karakteri ayrı ayrı tututyor
print("Liste: ",liste,"\nuzunluk: ",len(liste))

print("Listenin 2. elemanı(3): ",liste[2])
print("Sonuncu Eleman: ",liste[-1])                     #sonuncu eleman için -1 veriliyor, string ile aynı
print("Sonuncu Eleman: ",liste[len(liste)-1])           #Sonuncu elemanı yazdırmak için farklı teknik,[] kullanmayı unutma!

print(liste[0:])                                        #0. elemandan başla sonuna kadar[başlangıç:son:artış], Tersten yazdırmak için -artış deüer,n, -1 gir, stringlerde de geçerli
 """

    ### liste metodları
""" 

liste.append(1)                                         #listeye eleman ekleme (sadece 1 eleman)(en son)
liste.append(2)
print(liste)

liste.pop()                                             #değer verilmezse en sondaki elemanı siler
print(liste)
liste.pop(10)                                           #indis numarasını siler 'A'
print(liste)

siralanacakliste =[9,8,7,6,5,774,4,3,2,1,0]
siralanacakliste.sort()                                 #sıralama
print(siralanacakliste)

siralanacakliste.sort(reverse = True)                   #tersten sıralama
print(siralanacakliste)

###iç içe liste
liste = [[1,2],[3,4],[5,6]]
print(liste[1])

print(liste[1][1])

 """

                                                #########################Demetler - Tuples(DEĞİŞTİRİLEMEZ ve PARANTEZ ile tanımlanır)


""" demet = (1,2,3,4,5,6,7,8,9)
print(type(demet))

print("Tuple'ın 4. eleman: ",demet[4])

demet2 = (1,2,3,4,5,5)

print("{0} sayısı tuple'ın içinde {1} defa var".format("5",demet2.count(5)))                    #count fonksiyonu

demet3 = ("Python", "Java", "Javascript")
print("{0}'un tuple'ın içindeki index numarası: {1}".format("Python",demet3.index("Python")))   #index fonksiyonu

print("{0}'un tuple'ın içindeki index numarası: {1}".format("Javascript",demet3.index("Javascript")))
 """


                                                                        ################################    Dİctionary-sözlük

""" 
sozluk1 = {"bir":1,"iki":2,"üç":3,"dört":4}
print(sozluk1)
print(type(sozluk1))

#boş oluşturmak
sozluk2 = dict()
print(sozluk2)

print("dict'in içinde bir değerinin karşılığı: ",sozluk1["bir"])
print("dict'in içinde iki değerinin karşılığı: ",sozluk1["iki"])

sozluk1["beş"] = 5
print(sozluk1)

print(sozluk1.keys())           #anahatar isimlerini alma
print(sozluk1.values())         #değerleri alma
print(sozluk1.items())          #tuple olarak alma alma
 """

#####################   Kullanıcıdan girdi alma - input!!!!


""" 
sayi = input("Sayı bir len mQ: ")
print("Girdiğiniz sayı: {0} mı ? ".format(sayi))
print("girdiğiniz sayının tipi: ",type(sayi))


                                ####Girilen input değeri string olarak algılanıyor. Sonradan tür dönüşümü yapılması gerekiyor

a = int(input("Sayı gir amk: "))
print("girdiğiniz sayının tipi: ",type(a))
 """


""" 
try:
        b = int(input("Sayı gir amk: "))
        print(b)
except ValueError:
        print("Lütfen sadece sayı giriniz")

print("fixed")
 """


                                                                                                ##########Mantıksal değer-ifade


#Boolean

""" 

a = True;
print(a,type(a))

b = False;
print(b,type(b))

print(bool(3))  #0'dan farklı olan her sayı için True, 0 olanlar için False değeri döner
print(bool(0))

c = None                #Sonradan değer atamak istersek kullanabiliriz, null yerine geçmiştir
print(c)

 """


                                                                        #Karşılaştırma Operatörleri


""" 

print(1 == 1, 1==2)        #       ==      eşit mi ? 
print(3!=4)        #       !=      eşit değil mi ? eşit değilse true döner
print(7>3)        #       >       soldaki değer sağdakinden büyük mü ?
print(7<8)        #       <       soldaki değer sağdakinden büyük mü ?
print(12>=15, 12>=12, 12>=10)        #       >=      soldaki değer sağdaki değerden büyük veya eşit mi ?
print(7<=9, 7<=7, 7<=4)        #       <=      soldaki değer sağdaki değerden küçük veya eşit mi ?



#Mantıksal Bağlaçlar And - Or - Not operatörü

# koşul and koşul ========> Koşullardan birisi false ise false döner. Çarpma işlemi gibi
# koşul or koşul =========> Koşullardan birisi true ise true değeri döner


print(1<2 and 3.4 == 35)                #Bir tanesi false olduğu için false döndü 
"""




""" 

#String karşılaştırmasında alfabetik sıraya göre karşılaştırma yapılır.
print("String karşılaştırması: ","Canberk" < "Oğuz")


print(3>2 and "Alp" == "Alp")           #İkisi de True olduğu için True döndü

print(74>47 or "Bum" == "Be Yarag")     #Birisi True olduğu için True döndü    

print(not 2==2)                         #tersine çeviriyor


# If-Else-Elif yapısı (matOperatorOrnek.py adlı dosyada var)

"""




""" 
#Girilen sayıdan en büyüğünü bulma
sayi1 = int(input("İlk Sayı: "))
sayi2 = int(input("İkinci Sayı: "))
sayi3 = int(input("Üçüncü Sayı: "))

if(sayi1>sayi2 and sayi1>sayi3):
        enbuyuk = sayi1
        print("En büyük sayı:",enbuyuk)

elif(sayi2> sayi1 and sayi2>sayi3):
        enbuyuk = sayi2
        print("En büyük sayı:",enbuyuk)

elif(sayi3>sayi2 and sayi3>sayi1):
        enbuyuk = sayi3
        print("En büyük sayı:",enbuyuk)

else:
        print("Hata")

 """

        ##########################################################DÖNGÜLER!!!!!!!########################################################


#in operatörü - Listede, demette, string'te değer kontrolü yapar ve true, false değeri döner

# a="a" in "merhaba"
# print(a)


#For dögnüsü

""" 
dizi = ["Gaziantep","Adana","Mersin","Antalya","İzmir"]
sayiDizisi = [1,2,3,4,5,6,7,8,9]

for i in dizi:
         print(i) 


print("Dizinin;")
for i in range(len(dizi)):         
        print("{}. elemanı: {}".format(i,dizi[i]))


sayiDizisi.sort(reverse = True)
for i in sayiDizisi:
        print(i)


c = [(1,2),(3,4),(5,6),(7,8),(9,10)]

for i,j in c:
        print(i,j)



liste = [2,1,10,2,23,1,56,3]
 
total = 0
for i in liste:
    if (not (i % 2 == 0)):
        total += i
 
print(total)


liste = [2,1,10,2,23,1,56,3]
 
for i in liste:
    if (not (i % 2 == 0)):
        print(i)
"""


#While döngüsü


""" 
i = 0
while (i <= 10):
        print(i)
        i += 1
 """


#range fonksiyonu

""" 
print(*range(0,20))     #0 ile 20 arasındaki sayıları yazdır, 20 hariç. Yazdırmak için * koyuyoruz      - Başlangıç, Bitiş, Artış 

print(*range(0,100,2))

print(*range(20,0,-1))
"""


""" 
liste = [1,2,3,4,5,6,7,8,9]
#listede gezinme uzun

for i in liste:
        print(i)

#for ile range fonksiyonu

for i in range(1,101):
        print(i)



 """


#break ========> döngüden çık.          continue ========> tek seferlik atla ama döngüye devam et


#list comprehension - listeleri üretmek ve oluşturmak için kolay yöntem


""" 
liste1 = [1,2,3,4]
liste1.append(5)


#liste1'den liste2'yi oluşturma

liste2 = list() #liste2 = list[] ===> ikisi de boş liste oluşturur

#uzun yöntem


for i in liste1:
        liste2.append(i)

print(liste2)

 

#kısa yöntem

liste3 = [1,2,3,4,5,6,7,"Alp"]

liste4 = [i for i in liste3]            # i | for i in liste3 şeklinde ikiye ayrılmış olarak düşünülebilir. Döngü kısmı aynı

print(liste4)
 


listeCift = [0,2,4,6,8]

listeCarpimCift = [i * 2 for i in listeCift]
print("Çift rakamların 2 ile çarpımları: ",listeCarpimCift)


listeTuple = [(1,2),(3,4),(5,6)]
listeMutli = list()


for i in listeTuple:                            #Demetleri komple liste olarak alma. İç içe 2 döngü - i aslında birer liste oluyor
    for j in i:
        listeMutli.append(j)
print(listeTuple)
print(listeMutli)


# listeTuple2 = [i*j for i,j in listeTuple]
# print("Demetli listenin çarpımını aktarma tamamlandı. Sonuçlar: ",listeTuple2)



s = "Python"

listeS = [i * 3 for i in s]
print(listeS)

"""

""" 

#iç içe listeler

liste1 = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
for i in liste1:
        print("i Liste: ",i)    #i değeri bir listenin tamamına eşit oluyor. i içerisinde gezinirsek listenin elemanlarına erişmiş oluruz
        for j in i:
                print("J: ",j)
                liste2.append(j)

#LC hali

liste3 = [i for i in liste1 for i in i ]
print(liste3)

 """





                                                        #Metod öğrenme tekniği

""" 
a = [1,2,3,4,5,6,7,8]

help(a.append)  #unutulan metodları bu şekilde öğrenebilirsin
help(a.insert)  #index sayısına göre değer eğleme

 """
                                                        #Fonksiyonlar

""" 
                                                                                                                                                        #fonksiyon tanımlama
                                                                                                                                                        sayi1 = int(input("İlk sayı: "))
                                                                                                                                                        sayi2 = int(input("İkinci sayı: "))

                                                                                                                                                        def topla(sayi1,sayi2):
                                                                                                                                                                return sayi1+sayi2

                                                                                                                                                        print(topla(sayi1,sayi2))

"""


                                                        #Fonksiyonlarda Default değeri tanımlama!!!
""" 
def selamlama(isim = "Alp"):    #isim değişkenini default olarak Alp yaptık. Değer dönderilmediği zaman default değeri kullanılacak!
        print("Selam ",isim)

selamlama()     #Değer göndermediğimiz için default değer yazılacak
selamlama("Övüş")

 """

                                                        #Esnek sayılar!!!!!!!   *

""" 
def toplama(*a):
        print(a)

toplama(1,2,3,4,5)
#sadece bir değerin fonksiyona verileceğini tanımlasak bile * işareti koyduğumuz için gönderdiğimiz bütün değerler tuple içerisine aktarıldı

 """





""" 
#işlem yapabilmek için a değişkeninin içerisinde for döngüsü ile gezinmemiz gerekiyor

def toplama(*a):
        toplam = 0
        for i in a:
                toplam += i
        print(toplam)

toplama(1,2,3,4,5,6,7,8,9)
"""




                                                        #Global ve Yerel Değişkenler



""" 
def fonksiyon():
        a = 10
        print(a)
print(a)                #Tanımladığımız fonksiyonun içerisindeki a değişkeni, fonksiyon sonlandıktan sonra bellekten silinir. O yüzden hata alıyoruz (Yerel Değişken)
"""




""" 
b = 5                   #Global olarak tanımlanıyor
def fonksiyon():
        print(b)
fonksiyon()             #b değişkeni global bir değişken olduğu için fonksiyonun içinde tanımlı olmamasına rağmen ekrana bastırıldı

 """



""" 
c = 10
def fonksiyon():
        c = 2
        print("Fonskyion içinde:",c)       #yerel(fonksiyon) olarak tanımlandığı için fonksiyon tanımlandıktan sonra silinir
fonksiyon()
print("Fonksiyon dışında:",c,sep ='=')        #global tanımlandığı için fonksiyon dışında 10 değerini döner

 """

""" 
#global ifadesi

d = 12
def fonk():
        global d        #global ifadesi, fonksiyonun içerisinden d değişkenine her yerden(global olarak) erişebilmemize olanak sağlıyor
        d = 6
        print(d)
fonk()
print(d)
 """



                                                #Lambda ifadeleri       - küçük fonksiyonlar için kullanılabilir

#list Comprehension gibi pratik bir yöntem ya da JS'deki arrow function gibi

#fonksyion_adı = lambda parametreler.. : (işlem)
""" 
toplama = lambda x,y : x+y

print(toplama(2,4))

"""



""" 
#asal bulma 1

def asalMi(sayi):

        tamBolen = 0            #toplam bölüm sayısını sayıyoruz, asal olma durumunu belirlemek için

        for i in range(1,sayi+1):

                asalMi = asalKontrol(sayi,i)    #verilen sayı ile i değerinin tam bölünüp bölünmediğini kontrol etmek için diğer fonksiyonu çağırıyoruz

                if(asalMi):
                        tamBolen += 1


        if(tamBolen > 2 or sayi == 0 or sayi == 1):          #sayı 2'den fazla bölündüyse veya 0 ise asal bloğun içine giriyoruz
                print("{} sayısı asal değil!".format(sayi))
        elif(tamBolen <= 2):
                print("{} sayısı asal!".format(sayi))


def asalKontrol(sayi,i):

        if(i>0):
                if (sayi % i == 0):
                         return True
                else:
                        return False
        
#fonksiyonu çağırma
for i in range(20):
        asalMi(i)


 """



""" 
#asal sayı bulma 2

def asalMi(sayi):
        if(sayi == 0 or sayi == 1):
                return False
        elif(sayi == 2):
                return True
        
        else:
                for i in range(2,sayi):
                        if(sayi % 2 == 0):
                                return False
                        
                        return True
        
for i in range(2000):
        sayi = i
        if(asalMi(i)):
                print(sayi,"Asaldır")
        else: 
                print(sayi,"Asal DEĞİL")
 """

""" 
#Tam bölenlerini bulma
def tamBolenBulma(sayi):
        tamBolenListe = []
        for i in range(1,sayi+1):
                if(sayi % i == 0):
                        tamBolenListe.append(i)
        return tamBolenListe    #dışarı döndermek istediğimiz değeri return ediyoruz
                

for i in range(1,20):
        print(i,"Sayısının bölenleri:",tamBolenBulma(i))

 """


                                                #Modül kullanımı (kütüphane)

""" 
#import anahtar kelimesi ile ekleniyor

import math     #math kütüphanesi, modülü tanımlanıyor


# value = dir(math)       #dir metodu, modülün içerisindeki fonksiyonları gösteriyor
print(help(dir))        

print(help(math))       #math kütüphanesinin ne işe yaradığını gösteriyor

a = math.floor(5.7)             #floor, girdiğimiz değerden en küçük tam sayıyı dönüyor (aşağıya doğru yuvarlama)
print(a)

 """



""" 
                                                #Modüle kütüphaneye takma isim verme

import math as islem

b = islem.floor(5.7)
print(b)

 """

                                        #modülün ismini her yerde kullanmamıza gerek kalmayan tanımlama yöntemi 

""" 
from math import *              # * hepsi anlamına geliyor. Sadece kullanmak istediğimiz fonksiyonları yazabiliriz. or: factorial,sqrt,floor

c = floor(5.9)
print(c)

 """



#aynı isimde kendi fonksiyonumuzu import'tan sonra tanımlayarak çalıştırabiliriz. Import'tan önce tanımlarsak kütüphanenin fonksiyonu çalışır!

""" 
#Kendi modülünü dahil etme

import modul1                   #aynı dizinde modul1.py dosyasını dahil ediyoruz

print("3,4,5 sayılarının toplamı: ",modul1.toplama(3,4,5))
modul1.selamDur("Alp")
print(modul1.programming_languages)

"""









# Sayı tahmin oyunu v1
""" 
import random # "from random import randint" yazılabilirdi
import time

giris = "****************************\n\nSayı tahmin oyununa hoşgeldin\n\n1 ile 40 arasında rastgele sayı seçilecek ve sizin bu sayıyı bulmanız gerekiyor\n\n***************************************"
print (giris.title())


rastgele_sayi = random.randint(1,40)

while True:
        deneme_sayisi = 7
        kullanici_sayi = int(input("Lütfen 1-40 arasında bir sayı tutunuz: "))

        if (rastgele_sayi > kullanici_sayi):
                print("yükleniyor...\n")
                time.sleep(1)                   #1 saniye bekleme
                print("Yüklendi!!!\n")
                time.sleep(1)
                print("Daha büyük sayı giriniz\n\n")
                deneme_sayisi -= 1
        elif (rastgele_sayi < kullanici_sayi):
                print("yükleniyor...\n")
                time.sleep(1)                   #1 saniye bekleme
                print("Yüklendi!!!\n")
                time.sleep(1)
                print("Daha küçük sayı giriniz\n\n")
                deneme_sayisi -= 1
        else:
                print("Kontrol ediliyor...\n")
                time.sleep(1)
                print("Kontrol tamamlandı\n\n\n\n")
                time.sleep(1)
                print("Tebrikler kazandınız!!!!!!!!")
                break
        if(deneme_sayisi == 0):
                print("Deneme hakkınız kalmadı")
                time.sleep(1)
                print("Sayımız: ",rastgele_sayi)
                time.sleep(1)
                break
 """





# Sayı tahmin oyunu v2
""" 

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
"""
        
























