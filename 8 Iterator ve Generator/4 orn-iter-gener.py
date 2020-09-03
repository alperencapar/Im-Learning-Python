#kareler isimli class tanımşa ve iterable olsun. 
#init fonksiyonu maksimum isimli bir tane parametre alsın ve her next işleminde ekrana üzerinde bulunduğunuz sayının karesi yazdırılsın 


class Kareler():

    def __init__(self,max):
        self.max = max
        self.sayi = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.sayi += 1
        if (self.sayi <= self.max):
            sonuc = self.sayi ** 2
            return sonuc
        else:
            self.sayi = -1
            raise StopIteration

    
kareler = Kareler(5)
# for i in kareler:
#     print(i)





