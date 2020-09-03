#birinci parametre olarak true yada false değeri dönen değer alır. 2. parametre ise listedir. For döngüsü olmadan bütün listede ilk işlemi yapar


ciftsayi = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8,9,10]))

print(ciftsayi)




def asal_mi(x):
    i = 2
    if (x == 1):
        return False
    elif(x == 2):
        return True
    else:

        while(i < x):
            if(x % i == 0):
                return False

            i += 1

        return True

print("Asal sayılar: ",list(filter(asal_mi, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])))
print("2 Asal sayılar: ",list(filter(asal_mi, range(1,100))))