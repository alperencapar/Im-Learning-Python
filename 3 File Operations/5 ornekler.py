s = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

#Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın

frekans = dict()

for i in s:
    if(i in frekans):
        frekans[i] +=1
    else:
        frekans[i] = 1
    
    for i,j in frekans.items():
        print(i,": ",j)







#"şiir.txt" şeklinde bir dosya oluşturun ve bu dosyanın herbir satırını okuyun. 
#Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve bu string'i ekrana yazdırın

with open("siir","r",encoding="UTF-8")as file2:
    bas_harf= ""
    for i in file2:
        bas_harf += i[0]
    print(bas_harf)






#Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.

#                   coskun.m.murat@gmail.com
#                   example@xyz.com
#                   mustafa.com
#                   mustafa@gmail
#                   kerim@yahoo.com


with open("mailler.txt","r",encoding="UTF-8") as file:
    for satir in file:
        satir = satir[:-1]

        if(satir.endswith(".com") and satir.find("@") != -1):
            print(satir)
        



#https://nbviewer.jupyter.org/github/mustafamuratcoskun/Sifirdan-Ileri-Seviyeye-Python-Programlama/blob/master/İleri%20Seviye%20Veri%20Yapıları%20ve%20Objeler/İleri%20Seviye%20Veri%20Yapıları%20ve%20Objeler%20-%20Ödev%20ve%20Çözümleri/Programlama%20Ödevi%20Çözümleri%20-%20İleri%20Seviye%20Veri%20Yapıları%20ve%20Objeler.ipynb
