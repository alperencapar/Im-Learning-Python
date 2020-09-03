# dosyalar

# dosya açmak için open() fonksiyonu kullanıyoruz

#open(dosya_adı,erişme türü)    erişim türleri ===== >>> "w" (write) ,"r" (read) ,"a" (append)

# "w" ====>> oluşturmak istediğimiz dosya dizinde yoksa oluşturuyor. DOsya varsa, "SİLİP" tekrar oluşturuyor  (TEHLİKELİ!!!)

# "a" ====>> dosya dizinde yoksa, oluşturuluyor. Dosya mevcut ise yeniden oluşturmaz, dosyanın sonuna gider ve ekleme yapar

# file = open("bilgiler.txt","w",encoding ="UTF-8")           #encoding kısmı türkçe karakter ekleyebilmek için eklendi 



# file = open("C/Users/user/Desktop/bilgiler.txt","w")          #başka dizine kayıt etme


#dosyadaki her karakter 1 bayt'a eşittir

from time import sleep


""" 
if(open("bilgiler.txt","w")):
    print("Dosya açıldı")
else:
    print("Dosya açılamadı")

file.write("Vites ALP\n")     #9 bayt
file.write("Aykürt singilii\n")         #türkçe karakter ekleyebiliyoruz (encoding)
 """



# file = open("bilgiler.txt","a", encoding = "UTF-8")

# if(file):
#     print("Dosya açıldı")
# else:
#     print("Dosya açılamadı")

# file.write("Hamsi Ali\n")

# file.write("Bayburt Bayram\n")


""" 

file.close()        #dosya kapatma (MUTLAKA KAPATILMALI)
if(file.close):
    print("Dosya kapatılıyor...")
    sleep(1)
    print("Dosya başarılı bir şekilde kapatıldı ")
else:
    print("Dosya kapatılamadı")

 """











                            #dosya okuma işlemleri
"""
# file = open("bilgiler.txt","a", encoding = "UTF-8")
file = open("bilgiler.txt","r", encoding = "UTF-8")



print("Dosya Okunuyor...")
# icerik = file.read()
sleep(1) 
print("Dosya:")
# print(icerik,end ="")

# print(file.readline())      #tekli satır okuma

bilgilerListe = file.readlines()    #satırların hepsini liste olarak dönderiyor

print(bilgilerListe)

file.close()
"""











""" 
                    #Otomatik dosya kapatma


#with open(dosya_adi,erişim_türü) as file:
#    print("dosya işlemleri")

with open("bilgiler.txt","r",encoding = "UTF-8") as file: #dosya açıldı
    for i in file:
        print(i, end="")
#dosya kapandı
 """













#dosyanın hangi byte üzerinde olduğunu tell() fonksiyonu ile öğreniyoruz
#istediğimiz byte'a göndermek için ise seek() fonksiyonu kullanıyoruz
""" 
with open("bilgiler.txt","r",encoding = "UTF-8") as file:
    print(file.tell())
    file.seek(20)
    print(file.tell()) 
"""

""" 
with open("bilgiler.txt","r",encoding = "UTF-8") as file:
    file.seek(5)
    icerik = file.read(10)      #10 byte oku 
    print("Dosya: ",icerik)
    print("{}. byte üzerinde ".format(file.tell()))



 """













                    #Dosyalarda değişiklik
""" 
#en sona ekleme yapma
with open("bilgiler.txt","a",encoding = "UTF-8") as file:
    file.write("İbo\n")

with open("bilgiler.txt","r",encoding = "UTF-8") as file:
    print(file.read())

 """















""" 
                #dosyaların başında değişiklik yapmak

with open("bilgiler.txt","r+",encoding = "UTF-8") as file:
    icerik = file.read()
    icerik ="Gerard Butler\n" + icerik          #icerik değişkenine dosyayı aktarıyoruz sonra değişkenin başına ekleme yapıp kendisini de ekliyoruz
    print(icerik)


 """










#dosyaların ortasında değişiklik yapmak         - insert
""" 
with open("bilgiler.txt","r+",encoding = "UTF-8") as file:
    liste = file.readlines()
    liste.insert(4,"Ne bakiyun kardeeeşş\n")          #4. index'e ekleme yapıyoruz
    file.seek(0)

    # for i in liste:   #eklediğimiz değerle birlikte komple listeyi dosyaya geri yazdırıyoruz
    #     file.write(i)
                                #for yerine
    file.writelines(liste)



with open("bilgiler.txt","r+",encoding = "UTF-8") as file:

    print("LİSTE::::\n\n",file.read()) 



 """


""" 

def not_hesapla(satir):
    satir = satir[:-1]      #dosyanın her satırından sonra gelen "\n" karakterini siliyoruz
    liste = satir.split(",")        #split fonksiyonu gelen bilgileri , işaretine göre bölüyor ve bir listeye ekliyor
    isim = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    son_not = (not1 * 0.2) + (not2 * 0.2) + (not3 * 0.6)

    if (son_not >= 90):
        harf_notu = "AA"
    
    elif (son_not >= 85):
        harf_notu = "BA"

    elif (son_not >= 80):
        harf_notu = "BB"
        
    elif (son_not >= 75):
        harf_notu = "CB"

    elif (son_not >= 70):
        harf_notu = "CC"
        
    elif (son_not >= 65):
        harf_notu = "DC"
        
    elif (son_not >= 60):
        harf_notu = "DD"

    elif (son_not >= 55):
        harf_notu = "FD"

    else:
        harf_notu = "FF"

    return isim + "---------------> " + harf_notu + "\n"



with open("dosya.txt","r",encoding = "UTF-8") as file:
    eklenecek_listesi = []
    for i in file:
        eklenecek_listesi.append(not_hesapla(i))


with open("harf_not_listesi.txt","w", encoding="UTF-8") as file2:
    for i in eklenecek_listesi:
        file2.write(i)


"""




