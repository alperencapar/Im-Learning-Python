#zip fonksiyonu 2 tane listeyi birbirine gruplamayı sağlıyor

liste1 = [1,2,3,4,5]
liste2 = [6,7,8,10,11]

i = 0
sonuc = list()
while (i< len(liste1) and i < len(liste2)):
    sonuc.append((liste1[i],liste2[i]))
    i += 1
print(sonuc)




print(list(zip(liste1,liste2)))




liste_1 = [1,2,3,4]
liste_2 = ["Python","Php","Java","Javascript"]


for i,j in zip(liste_1,liste_2):
    print(i,j)


