#iterable(üzerinde gezilebilecek,(for döngüsü))

# bir objenin iterable olması için hazır olan __iter()__ ve __next()__ metodlarının tanımlanması gerekiyor

""" 
liste = [1,2,3,4,5,6,7,8,9]
# print(dir(liste))   #__iter__

iterator = iter(liste)
# print(iterator)
print(next(iterator))

print(next(iterator))

 """




class Kumanda():

    def __init__(self,kanal_listesi):
        self.kanal_listesi = kanal_listesi
        self.index = -1
    
    def __iter__(self): #kumanda objesini iterator objesine eşitleme yapılıyor
        return self #obje

    def __next__(self):
        self.index += 1
        if self.index < len(self.kanal_listesi):
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration


kumanda = Kumanda(["ATV","TRT","FOX", "KANAL D"])

iterator = iter(kumanda)

# print(next(iterator))

for i in iterator:
    print(i)






