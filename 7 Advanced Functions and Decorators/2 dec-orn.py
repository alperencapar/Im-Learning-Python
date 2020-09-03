

def ek_tek_sayi(fonksiyon):
    def wrapper(liste):
        tek_liste = []
        for i in liste:
            if(i % 2 == 1):
                tek_liste.append(i)
        print("****************************************TEK SAYILAR****************************************")
        print(tek_liste)
        fonksiyon(liste)
    return wrapper
            


@ek_tek_sayi
def cift_sayi(sayi_listesi):
    cift_liste= []
    for i in sayi_listesi:
        if(i % 2 ==0 ):
            cift_liste.append(i)
    print("****************************************ÇİFT SAYILAR****************************************")
    print(cift_liste)

sayilar = range(0,1000)

cift_sayi(sayilar)