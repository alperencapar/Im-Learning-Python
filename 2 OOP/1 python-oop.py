from time import sleep 
class Motosiklet():

    
    

    
    model = "Honda CBR 600RR"
    renk = "Gümüş"
    bg = 119
    agirlik = 184
    motor_hacmi = 599
    

   
            #objeler oluşturulurken çağrılan ilk metottur.
            #parametrelere default değeri ekleyebilriz ör. (model="Bilgi yok", renk="Movie-star",motor_hacmi="599",bg="119")
    def __init__(self,model,renk,motor_hacmi,bg):    #Self parametresi, her metodun başında bulunması gereken bir parametre. 
                                                    #Self, sınıfın geçerli örneğine bir referanstır ve sınıfa ait değişkenlere erişmek için kullanılır.
                                                    #self objeyi gösteren referanstır!!!!!!!!!!!!!
        sleep(0.7)
        print("init çalışıyor")
        sleep(2)
        self.model = model      #objemiz üzerinde model oluşturuyoruz(self.model) ve bu objeye model değerini eşitliyoruz
        self.renk = renk
        self.motor_hacmi = motor_hacmi
        self.bg = bg










 
motosiklet3 = Motosiklet("Honda CBR 600RR","Mavi-Beyaz",599,119)        #Motosiklet() Class'ından motosiklet3 objesi oluşturuluyor
print(motosiklet3.model,motosiklet3.renk,motosiklet3.motor_hacmi,motosiklet3.bg)


motosiklet4 = Motosiklet("Honda CBR 1000RR","Mavi-Beyaz",999,190)
print(motosiklet4.model,motosiklet4.renk,motosiklet4.motor_hacmi,motosiklet4.bg)













