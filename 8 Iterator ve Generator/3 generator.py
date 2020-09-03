# Generatorlar Pythonda iterable objeler (örnek olarak fonksiyonlar) oluşturmak için kullanılan objelerdir
#Bellekte herhangi bir yer kaplamazlar


def kareleri_al():
    sonuc = []
    for i in range(1,6):
        sonuc.append(i ** 2)
    
    return sonuc
    #hesapladığımız değereri sonuc adlı listeye attık ve hafızada yer tuttu

#print(kareleri_al())


def kareleri_al2():

    for i in range(1,6):
        yield i ** 2

generator = kareleri_al2()
iterator = iter(generator)

# for i in generator:
#     print(i)

#iki şekilde de olur

# for i in kareleri_al2():
    # print(i)



def carpim_tablos():
    for i in range(1,11):
        print("******")
        for j in range(1,11):
            yield "{} x {} = {}".format(i,j,i*j)

for i in carpim_tablos():
    print(i)


