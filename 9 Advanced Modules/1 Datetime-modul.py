from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL,"")  #bulunduğumuz konuma göre ayarlama



""" 

#https://nbviewer.jupyter.org/github/mustafamuratcoskun/Sifirdan-Ileri-Seviyeye-Python-Programlama/blob/master/İleri%20Seviye%20Modüller/DateTime%20Modülü.ipynb
#https://docs.python.org/2/library/time.html

print(datetime.now())



suan = datetime.now()

print(suan.year)
print(suan.month)
print(suan.microsecond)
print(suan.hour)


print(datetime.ctime(suan)) 
"""
""" 
suan = datetime.now()
print(datetime.strftime(suan,"%Y"))     #yıl
print(datetime.strftime(suan,"%B"))     #ay
print(datetime.strftime(suan,"%A"))     #gün ismi
print(datetime.strftime(suan,"%X"))     #saat
print(datetime.strftime(suan,"%D"))     #gün bilgisi



suan = datetime.now()
saniye = datetime.timestamp(suan)           #saniye cinsinden alma
print(saniye)

suan2 = datetime.fromtimestamp(saniye)      #saniyeden tarihe çevirme
print(suan2)
 """

# iki tarih arasındaki fark


birth = datetime(1999,4,21)         #Yıl,Ay,Gün


suan = datetime.now()

print(suan - birth )


