import os 

#işletim sisteminde işlemler gerçekleştireibliyoruz

# print(os.getcwd())  #os modülünün bulunduğu konum

#os.chdir("C:/Users/alper/Desktop/Python/Learning Phase Codes")    #change directory(dizin değiştirme)
# print(os.getcwd()) 


# print(os.listdir())     #bulunduğu dizindeki dosyaları listeler (list directory)


# os.mkdir("Deneme1")  #klasör oluşturma (make directory)


# os.makedirs("Deneme2/Deneme3")  #iç içe klasör oluşturabiliyor. mkdir ile arasındaki fark bu

# os.rmdir("Deneme2/Deneme3")     #klasör silme remove directory


# os.removedirs("Deneme2/Deneme3")    #ikisini de silme


# os.rename("text.txt","test.txt")    #yeniden adlandırma (orjinal isim, yeni isim)



# print(os.stat("test.txt"))  #bilgileri alınıyor



# print(os.stat("test.txt").st_mtime)     #st_mtime ===== değiştirilme zamanı saniye cinsinden veriliyor. datetime modülündeki fromtimestamp fonksiyonu ile tarih alınabilir


# for i in os.walk("C:/Users/alper/Desktop"):     #bütün dosyaları liste şeklinde alma
#     pass


# for klasor_yolu, klasor_isimleri,dosya_isimleri in os.walk("C:/Users/alper/Desktop"):
#     print("Klasör yolu: ",klasor_yolu)
#     print("Klasör ismi: ",klasor_isimleri)
#     print("Dosya ismi: ",dosya_isimleri)
#     print("************************************************")


for klasor_yolu, klasor_isimleri,dosya_isimleri in os.walk("C:/Users/alper/Desktop"):
    for i in dosya_isimleri:                    #masaüstü içindeki bütün dosya isimleri
        if(i.endswith(".txt")):                  #dosyaların sonu txt ile biityorsa(sadece txt dosyalarını alma)
            print(i)




