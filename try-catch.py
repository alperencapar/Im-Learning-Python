# print(a)        #daha önce a değişkeni tanımlanmadığı için bize hata dönecek
#NameError: name 'a' is not defined hatasını döndü


# print(int("12ada1512")) #ValueError değeri dönecek, çünkü harfleri tamsayı değerine dönüştüremiyoruz

# print(2/0)              #ZeroDivisionError dönecek çünkü hiçbir sayı 0'a bölünemez

#bu hataları programın içerisinde yakalayıp, hataya göre işlem yapabilmek için 
#try-except-finally anahtar kelimeleri kullanırız

""" 
try:
    print(a)
    print(int("12ada1512"))
    print(2/0)
    #hata çıkabilecek kodlar buraya yazılır
    #hata çıkarsa program except bloğuna girecek
    #hata olursa try bloğundaki diğer işlemler çalışmayacak
except (NameError,ValueError,ZeroDivisionError):
    print("hata oluştu ve except bloğu çalıştırıldı")
    #NameError hatası oluşunca burası çalışacak
 """

#finally
#Mutlaka çalışması gereken kodları bu bloğa yazıyoruz


#raise 
#kendi yazdığımız fonksiyonlar yanlış kullanılırsa kendi hatamızı raise ile üretebiliriz

def terscevir(string):
    if (type(string) != str):
        raise NotString("String değer girin!")
    else: 
        return string[::-1]

# print(terscevir("Alpcusta"))
# print(terscevir(34))


try:
    print(terscevir(12))
except NameError:
    print("String hatası girildi")



