                                #https://www.tutorialspoint.com/python3/python_strings.htm


#upper() metodu stringin tüm karakterlerini büyük harfe çevirir.
print("python".upper())
#lower() metodu stringin tüm karakterlerini küçük harfe çevirir.
print("python".lower())

 
#replace(x,y) : Stringteki x değerlerini y ile değiştirir

print("Herkes ana baba bacı gardaş".replace("a","o"))

print("Python Programlama Dili".replace(" ","-"))



#startswith(x) : String x ile başlıyorsa True, başlamıyorsa False değeri döndürür.

#endswith(x) : String x ile bitiyorsa True, bitmiyorsa False değeri döndürür.


print("Python".startswith("Py"))
print("Python".endswith("on"))


#split(a) : Verilen bir a değerine göre string parçalara ayrılarak herbir parça listeye atılır.

liste = "Python Programlama Dili".split(" ") # Boşluk karakterine göre ayrıldı.
print(liste)


#strip(x) : Stringin başında ve sonunda bulunan x değerlerini siler.

#lstrip(x) : Stringin sadece başında bulunan x değerlerini siler.

#rstrip(x) : Stringin sadece sonunda bulunan x değerlerini siler.


print("                   python                          ".strip())

print(">>>>>>>>>>>>>>Mustafa>>>>>>>>>>>>>>>>>>>>>>>>>>".strip(">"))



liste1 = ["21","02","2014"]
"/".join(liste)
print(liste1)


#count(x): Stringin içindeki x değerlerini sayar

print("ada kapısı yandan çarklı".count("a"))


#find(x) : x değerini baştan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.
print("araba".find("r"))




#rfind(x) : x değerini sondan itibaren string içinde arar ve bulursa ilk bulduğu indeksi döndürür. Bulamazsa "-1" değerini verir.

print("araba".rfind("r"))

