
class Vowels:
    def __init__(self,napis):
        self.napis = napis

    def __iter__(self):
        self.pozycja = 0
        return self

    def __next__(self):
        while self.pozycja < len(self.napis):
            litera = self.napis[self.pozycja]
            self.pozycja += 1
            if litera in "aeiouy":
                return litera
        raise StopIteration

x = input("Podaj napis: ")

for char in Vowels(x):
    print(char)





