class Dosya():



    def __init__(self):
        with open("metin.txt","r",encoding="UTF-8") as file:
            dosya_iceriği = file.read() #paragraf kompe geldi
            kelimeler = dosya_iceriği.split()       #kelimeler geldi ama boşluk ve . ile birlikte
            self.sade_kelimeler = list()            #self ile her yerden çağırabilir liste açıldı

            for i in kelimeler:
                i = i.strip("\n")       #kelimelerin alt satır boşluğunu aldık
                i = i.strip(" ")        #kelimelerin boşluğunu aldık
                i = i.strip(".")        #kelimelerin . işaretini aldık
                i = i.strip(",")        #kelimelerin , işaretini aldık

                self.sade_kelimeler.append(i)   #listeye ekliyoruz
            

    def tum_kelimeler(self):

        kelime_kumesi = set()

        for i in self.sade_kelimeler:
            kelime_kumesi.add(i)

        print("Tüm kelimeler....")
        for i in kelime_kumesi:
            print(i,"\n")
            print("*******************************")


    def kelime_frekans(self):
        kelime_sozluk = dict()
        for i in self.sade_kelimeler:
            if (i in kelime_sozluk):        #sözlüğün içinde aynı kelime var mı ?
                kelime_sozluk[i] += 1       #varsa anahtar sayısını 1 arttır
            
            else:
                kelime_sozluk[i] = 1

        for kelime,sayi in kelime_sozluk.items():
            print("{} kelimesi {} defa geçiyor".format(kelime,sayi))
            print("*******************************")




dosya = Dosya()
# dosya.tum_kelimeler()
dosya.kelime_frekans()