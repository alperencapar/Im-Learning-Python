liste = ["Elma","Armut","Muz","Kiraz"]

sonuc = list()

i = 0
while (i<len(liste)):
    sonuc.append((i,liste[i]))     #() demet yapmak için
    i += 1 

print(sonuc)

print(list(enumerate(liste)))


for i,j in enumerate(liste):
    print(i,j)



