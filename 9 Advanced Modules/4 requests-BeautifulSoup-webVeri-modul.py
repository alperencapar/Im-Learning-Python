#requests ve beautifulSoup modülü internetten indirmemiz gerekiyor
#pip3 install requests 
#pip3 install beautifulsoup4            #pip güncelleme pip3 install --upgrade pip

#web sayfalarından veri çekme

#https://nbviewer.jupyter.org/github/mustafamuratcoskun/Sifirdan-Ileri-Seviyeye-Python-Programlama/blob/master/İleri%20Seviye%20Modüller/Requests%20ve%20BeautifulSoup%20Modülü.ipynb


import requests
from bs4 import BeautifulSoup

url = "https://www.obilet.com/seferler/377-382/2020-08-20"

response = requests.get(url)
html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")
# print(soup.prettify())
""" 
for i in soup.find_all("a"):   #sadece a etiketini yazdıracak
    #print(i.get("href"))    #sadece href özelliğini al diyoruz
    print(i.text)       #sadece yazıları al diyoruz
    print("******************************************")
 """


print(soup.find_all("div",{"class":"partner col"}))     #div etiketlerinde class'ı partner col olanları al












