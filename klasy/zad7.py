import pytest


class Produkt(object):
    def __init__(self, id, nazwa, cena):
        self._ID = []
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        return f'Produkt "{self.nazwa}", id: {self._ID}, cena: {self.cena} PLN'
    def extend_id(self, ID):
        self._ID.append(self._ID)
        self.nazwa =operacja


def main():
    Przedmiot = Produkt()
    while True:
        komenda = input("""Wybierz opcje:[d] - dodaj do magazynu 
            [z] zakoncz """)
        if komenda == "d":
            przedmiot = input("Jaki produkt chcesz dodac? ")
            price = int(input(f"Jaką cene {przedmiot} chcesz dodac?")
        if komenda == "z"
            break




def test_product():
    Produkt = Produkt()
    Produkt.extend_id(["Woda", "Chleb", "Sok"])
    Produkt = Produkt(1, 'Woda', 10.99)

def test_product_print_info():
    product = Product(1, 'Woda', 10.99)
    assert product.print_info() == 'Produkt "Woda", id: 1, cena: 10.99 PLN'