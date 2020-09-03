from PIL import Image,ImageFilter
#image = Image.open("kuş.jpg")   #resmi ekleme

#image.show()        #gösterme

#image.save("kuş2.jpg")  #kopya oluşturma

#image.rotate(180).save("kuş3.jpg")      #180 derece döndür ve kayıt et

#image.convert(mode = "L").save("kuş5.jpg")      #siyah beyaz yapma


            #boyut düşürme

#degistir = (960,600)
#image.thumbnail(degistir)
#image.save("kuş6.jpg")


                #resim bulurlaştırma

#image.filter(ImageFilter.GaussianBlur(5)).save("kuş7.jpg")


#resim kırpma

image2 = Image.open("atatürk.jpg")
kirpilacak_alan = (340,0,950,600)
image2.crop(kirpilacak_alan).save("atatürk2.jpg")




