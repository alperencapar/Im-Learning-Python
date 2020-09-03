def not_hesaplama(satir):
    satir = satir[:-1]      #"\n" çıkarıldı
    liste = satir.split(",")        #gelen bilgiyi , işaretine göre böl ve listeye ekle

    isim = liste[0]
    vize1 = int(liste[1])
    vize2 = int(liste[2])
    final = int(liste[3])

    not_ortalama = (vize1 * 0.2) + (vize2 * 0.2) + (final * 0.6)
    
    if (not_ortalama >= 90):
        harf_notu = "AA"
    
    elif (not_ortalama >= 85):
        harf_notu = "BA"

    elif (not_ortalama >= 80):
        harf_notu = "BB"
        ""
    elif (not_ortalama >= 75):
        harf_notu = "CB"

    elif (not_ortalama >= 70):
        harf_notu = "CC"
        
    elif (not_ortalama >= 65):
        harf_notu = "DC"
        
    elif (not_ortalama >= 60):
        harf_notu = "DD"

    elif (not_ortalama >= 55):
        harf_notu = "FD"

    else:
        harf_notu = "FF"


    return isim + "," + harf_notu + "\n"


def listeyi_str_cevirme(liste):
    isim = liste[0]
    harf = liste[1]

    return isim + "," + harf +"\n"


with open("dosya.txt","r",encoding ="UTF-8") as file:
    eklenecek_liste = []
    for i in file:
        eklenecek_liste.append(not_hesaplama(i))


with open("not_listesi2.txt","w",encoding="UTF-8") as file2:
    for i in eklenecek_liste:
        file2.write(i)


with open("not_listesi2.txt","r",encoding="UTF-8") as file3:
    
    kalanlar = []
    gecenler = []
    for satir in file3:
        satir = satir[:-1]
        satir_liste = satir.split(",")

        if(satir_liste[1] =="FD" or satir_liste[1] =="FF"):
            kalanlar.append(satir_liste)
        else:
            gecenler.append(satir_liste)


with open("kalanlar.txt","w",encoding="UTF-8") as file4:
    for i in kalanlar:
        file4.write(listeyi_str_cevirme(i))
        # file4.write("\n")


with open("gecenler.txt","w",encoding="UTF-8") as file5:
    for i in gecenler:
        file5.write(listeyi_str_cevirme(i))
        # file5.write("\n")









