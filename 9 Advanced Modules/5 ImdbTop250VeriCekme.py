import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"
response = requests.get(url)
html_icerik = response.content

soup = BeautifulSoup(html_icerik,"html.parser")

basliklar = soup.find_all("td",{"class": "titleColumn"})
ratingler = soup.find_all("td",{"class": "ratingColumn imdbRating"})


#print(len(basliklar),len(ratingler))    #ikisi de 250 250 yani denkler


for baslik,rating in zip(basliklar,ratingler):      #zip iki listeyi birleştiriyor
    baslik = baslik.text
    rating = rating.text
    baslik = baslik.strip()
    baslik = baslik.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    print("Film: ",baslik)
    print("Rating: ",rating)



