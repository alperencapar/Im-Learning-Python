
#Kümeler, matematikte olduğu gibi bir elemandan sadece bir adet tutan bir veritipidir.

x =  set() # Boş küme

print(type(x))

liste = [1,2,3,3,1,1,2,2,2] # Aynı elemanı birçok defa  barındıran bir liste

x = set(liste) # Veri tipi dönüşümü

print(x)


#Kümeler de tıpkı sözlükler gibi sırasız bir veri tipidir. for döngüsüyle erişim sağlayabiliriz
#for döngüsü dışında index değeri ile erişim sağlayamıyoruz 


x = {"Python","Php","Java","C","Javascript"}

for i in x:
    print(i) 


#add() metodu, Kümeye eleman eklemimizi sağlar. Aynı eleman eklenmeye çalışırsa hata vermez ve herhangi bir ekleme işlemi yapmaz
x = {1,2,3}
x.add(4)
print(x)



#difference() metodu birinci kümenin ikinci kümeden farkını döner

kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}

print(kume1.difference(kume2))




#difference_update() metodu, birinci kümenin ikinci kümeden farkını dönerek birinci kümeyi bu farka göre günceller
kume1.difference_update(kume2)
print(kume1)



#discard() metodu, içine verilen değeri kümeden çıkartır
kume1 = {1,2,3,4,5,6}
kume1.discard(2)
print(kume1)



#intersection() iki kümenin kesişimleri bulmamızı sağlar
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}

print(kume1.intersection(kume2))




#intersection_update() metodu, birinci kümeyle ikinci kümenin kesişimlerini bulur ve birinci kümeyi bu kesişime göre günceller
kume1.intersection_update(kume2)
print(kume1)




#isdisjoint() metodu,  iki kümenin kesişim kümesi boş ise True, değilse False döner.
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
kume3 = {30,40,50}

print(kume1.isdisjoint(kume2))
print(kume1.isdisjoint(kume3))


#issubset() metod, birinci küme ikinci kümenin "ALT" kümesiyse True, değilse False döner
kume1 = {1,2,3}
kume2 = {1,2,3,4}
kume3 = {5,6,7}
print(kume1.issubset(kume2))
print(kume1.issubset(kume3))


#union() metodu, iki kümenin birleşim kümesini döner
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
print(kume1.union(kume2))



#update() metodu, birinci kümeyle ikinci kümenin birleşim kümesini döner ve birinci kümeyi buna göre günceller.
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}

kume1.update(kume2)
print(kume1)




