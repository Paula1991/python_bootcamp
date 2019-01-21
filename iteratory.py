class Iterator:
    def __init__(self,x):
        self.number = x

    def __iter__(self):
        self.licznik =0
        return self

    def __next__(self):
        if self.licznik > self.number:
            raise StopIteration
        liczba = self.licznik
        self.licznik +=1
        return liczba


x = int(input ("Podaj liczbę: "))
for number in Iterator(x):
    print(number)