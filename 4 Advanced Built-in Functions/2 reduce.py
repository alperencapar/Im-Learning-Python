#ilk parametre olarak fonksiyon objesi alıyor ve veri tipi değeri giriliyor(liste vs)
# fonksiyonu listenin ilk 2 elemanına uyguluyor ve sonucu 3. elemana uyguluyor

from functools import reduce

def toplama(x,y):
    return x+y


print(reduce(toplama,[12,18,20,10]))    #60 ====>> 12+18 = 30, 30+20 = 50, 50+10 = 60



print("5 Faktoriyel: ",reduce(lambda x,y: x * y, [1,2,3,4,5]))   #5 faktoriyel

print("6 Faktoriyel: ",reduce(lambda x,y: x * y, [1,2,3,4,5,6])) #6faktoriyel


def enbuyuk(x,y):
    if(x>y):
        return x
    else:
        return y
    


print("En büyük sayı: ",reduce(enbuyuk,[-2,1,2,3,4]))



