# map fonksiyonu içerisine bir tane fonksiyon alıyor ve içerisinde for döngüsü ile gezilebilecek veritipi alıyor

def double(x):
    return x*2


map(double,[1,2,3,4,5])         #listedeki bütün elemanlar for döngüsü olmadan double fonksiyonuna gidiyor ve işlem görüyor

#görüntülemek için;

ikikati = list(map(double, [1,2,3,4,5,]))     #map fonksiyonunu list'e çevirip değişkene aktarıyoruz
print(ikikati)



#tek satır fonksiyon için lambda kullanabiliriz


karesi = list(map(lambda x : x **2,(1,2,3,4,5)))
print(karesi)




liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10]
liste3 = [11,12,13,14,15]

coklu_liste= list(map(lambda x,y,z: x*y*z,liste1,liste2,liste3))
print(coklu_liste)