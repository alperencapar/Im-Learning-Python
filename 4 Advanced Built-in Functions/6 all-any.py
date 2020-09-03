def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True
            #bütün değerler True ise True en az birisi False ise False dönmek istiyoruz

liste = [True,False,True,False,True]
print(hepsi(liste))

liste2 = [True,True,True,True,True]
print(hepsi(liste2))


def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False

print(herhangi([True,False,True,False,True]))


print("all fonksiyonu: ", all(liste))       #all fonksiyonunda, bütün değer doğruysa True bir tane False ise False dönüyor
print("all fonksiyonu: ", all(liste2))



print("any fonksiyonu: ", any(liste))       #any fonksiyonunda bir değer bile True ise True değer dönüyor


