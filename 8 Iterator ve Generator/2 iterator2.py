""" 
class Kumanda():

    def __init__(self,kanal_listesi):
        self.kanal_listesi = kanal_listesi
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.kanal_listesi):
            return self.kanal_listesi[self.index]

        else:
            raise StopIteration

kumanda = Kumanda(["ATV","FOX","KANAL D","TRT"])
iterator = iter(kumanda)

for i in iterator:
    print(i) 
"""




"""  
class Moto():

    def __init__(self,moto_listesi):
        self.moto_listesi = moto_listesi
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index < len(self.moto_listesi):
            return self.moto_listesi[self.index]
        else:
            raise StopIteration

moto = Moto(["600RR","R6","1000RR","R1"])
iterator2 = iter(moto)

for i in iterator2:
    print(i)

 """
