#Faktöriyel hesaplama

# 5! = 5*4*3*2*1


while True:
    sayi = (input("Hesaplanacak sayıyı giriniz: "))
    if(sayi == "q"):
        break
    else:
        sayi = int(sayi)
        faktoriyel = 1
        for i in range(2,sayi+1):
            faktoriyel *= i
            
        print("Faktoriyel: ",faktoriyel)

