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
        print("Vücut Kitle İndexiniz: {} Sonuç: {}".format(kitleIndex,"Süper Morbid Obez"))

else:
    print("Hesaplanamadı!!!")


