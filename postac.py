class Postac():
    def __init__(self,imie,atak,zdrowie):
        self.imie = imie
        self.atak = atak
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie

    def przedstaw_sie(self):
        print(self)

    def __str__(self):
        return(f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia")


rufus = Postac ("Rufus",3,100)
rufus.przedstaw_sie()
print(rufus)