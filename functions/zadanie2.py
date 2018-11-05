
def wiecej_niz(napis,liczba_razy):
    while True:
        napis = input("Podaj napis: ")
        liczba_razy = input("Podaj liczbe razy: ")
        for litera in napis.lower():
            if count(napis)>liczba_razy:
                return True

liczby = set()

while True:
    tekst = input("Wprowadź liczbę lub k by zakończyć: ")
    if tekst.lower() == 'k':
        break
    else:
        liczba = int(tekst)
        liczby.add(liczba)

def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("",0)=set()