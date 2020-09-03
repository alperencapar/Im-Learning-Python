""" 
    2. dereceden bir bilinmeyenli denklemin köklerini bulma

    Denklem: ax^2 + bx + c                      # ^(üs) işareti python'da ** olarak kullanılıyor !!!

    Delta Hesaplama: b ** 2- 4 * a * c                  ** = kare

    Birinci kök: ( -b - delta ** 0.5) / (2*a)

    İkinci Kök: ( -b + delta ** 0.5) / (2*a)

"""

""" 

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b ** 2- 4 *a *c

x1 = (-b - delta ** 0.5) / (2*a)
x2 = (-b + delta ** 0.5) / (2*a)

print("Birinci Kök: {}\nİkinci Kök: {}\n".format(x1,x2))


print("Normal üs alma: ",a^b)
print("** iles alma: ",a**b) 

"""

#problem 1

# Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın
""" 
x1 = int(input("Birinci sayi: "))
x2 = int(input("İkinci sayi: "))
x3 = int(input("Üçüncü sayi: "))

sayilar = [x1,x2,x3]

print("\nİlk sayı: {}\nİkinci sayı: {}\nÜçüncü sayı: {}".format(sayilar[0],sayilar[1],sayilar[2]))
print("Sayıların çarpımı: {}".format(sayilar[0]*sayilar[1]*sayilar[2]))

 """



#Problem 2
""" Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

 """
 
""" 
boy = float(input("Boyunuzu metre cinsinden giriniz(1.77): "))
kilo = float(input("Kilonuzu giriniz(83.0): "))

kitleIndex = kilo / (boy * boy)

if (kitleIndex <= 18.4 ):
    print("Vücut Kitle İndexiniz: {} Sonuç: {}".format(kitleIndex,"Zayıf"))

elif (kitleIndex > 18.4 and kitleIndex <= 24.9):
    print("Vücut Kitle İndexiniz: {} Sonuç: {}".format(kitleIndex,"Normal"))

elif (kitleIndex > 24.9 and kitleIndex <= 29.9):
    print("Vücut Kitle İndexiniz: {} Sonuç: {}".format(kitleIndex,"Fazla Kilolu"))

elif (kitleIndex > 29.9 and kitleIndex <= 34.9):
    print("Vücut Kitle İndexiniz: {} Sonuç: {}".format(kitleIndex,"Obez"))

elif (kitleIndex > 34.9 and kitleIndex <=39.9):
    print("Vücut Kitle İndexiniz: {} Sonuç: {}".format(kitleIndex,"Morbid Obez"))

elif (kitleIndex > 39.9):
        print("Vücut Kitle İndexiniz: {} Sonuç: {}".format(kitleIndex,"Süper Allahu Ekber Obez"))

else:
    print("Hesaplanamadı!!!")


 """

    #Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin
""" 
a = int(input("Sayı Bir: "))
b = int(input("Sayı İki: "))
print(a,b)
a,b = b,a
print(a,b)
    
 """


""" 
#Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın

yakan_miktar = float(input("Kilometrede yakan miktar:"))

kilometre = int(input("Kaç km yol yaptınız:"))

print("Tutar: {} tl".format(yakan_miktar * kilometre))
"""