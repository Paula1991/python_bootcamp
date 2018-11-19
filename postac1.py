from random import randint
from przedmiot import Przedmiot

# randint (1,10) losowa liczba calkowita z przedzialu 1-10

class Postac():
    def __init__(self,imie,atak,zdrowie):
        self.imie = imie
        self.atak = atak
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.ekwipunek = []

    def przedstaw_sie(self):
        print(self)

    def __str__(self):
        if self.czy_zyje():
            napis ="EWKIPUNEK\n"
            for x in self.ekwipunek:
                napis += str(x) + "\n"
            return f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia.\n" +napis
        else:
            return f"Jestem {self.imie} , miałem {self.atak} ataku i nie zyje"


    def leczenie(self,ile):
        if self.czy_zyje():
            print (f"{self.imie} został uleczony za {ile} punktow zycia")
            self.zdrowie = self.zdrowie + ile
            if self.zdrowie > self.max_zdrowie:
                self.zdrowie = self.max_zdrowie
        else:
            print (f"{self.imie} nie mogł zostać wyleczony i nie żyje")



    def obrazenie(self,ile):
        print (f"{self.imie} oberwał za {ile} obrazen")
        self.zdrowie = self.zdrowie - ile
        if self.zdrowie <0:
            self.zdrowie = 0
        pass

    def czy_zyje(self):
        return self.zdrowie >0

    def moc_ataku(self):
        wynik = randint(self.atak//2,self.atak)
        return wynik

     def daj_przedmiot(self,przedmiot):
         self.ekwipunek.append(przedmiot)


    @staticmethod
    def walka(atakujacy,broniacy):
        print (f"Walka : {atakujacy.imie} vs {broniacy.imie}")
        while atakujacy.czy_zyje() and broniacy.czy_zyje():
            print(atakujacy)
            print(broniacy)
            atak_atakujacego = atakujacy.moc_ataku()
            atak_broniacego= broniacy.moc_ataku()
            print(f"{atakujacy.imie} uderza {broniacy.imie} za {atakujacy.atak} obrazen")
            broniacy.obrazenie(atakujacy.atak)
            print(f"{broniacy.imie} uderza {atakujacy.imie} za {broniacy.atak} obrazen.")
            atakujacy.obrazenie(broniacy.atak)
        print ("Koniec walki")


rufus = Postac ("Rufus",30,100)
grazyna = Postac ("Grażyna",40,800)

tulipan = Przedmiot ("Zielony tulipan zniszczenia",5)
rufus.daj_przedmiot(tulipan)

Postac.walka(rufus,grazyna)
print(rufus)
print(grazyna)
# obrazenia=(5)
# rufus.przedstaw_sie()
# print(rufus)
# rufus.obrazenie(40)
# print(rufus)
# rufus.obrazenie(80)
# print(rufus)
# rufus.leczenie(120)

def test_nowa_postac():
    postac = Postac("Albert",1,20)

    assert postac.imie == "Albert" and postac.atak == 1 and postac.zdrowie == 20 and postac.max_zdrowie == 20

def test_obrazenia():
    postac = Postac ("Rafał",5,200)
    assert postac.zdrowie ==200
    postac.obrazenie(80)
    assert postac.zdrowie == 120
    postac.obrazenie(200)
    assert postac.zdrowie == 0

def test_leczenie():
    pass

def test_leczenie_nieboszczyka():
    pass

# def test_za_duze_leczenie():
#     postac = Postac("Rafal",5,200)
#     postac.obrazenie(80)
#     assert postac.zdrowie ==120
#     postac.wylecz()
#     pass
