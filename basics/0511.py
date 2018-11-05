

co_na_co={
    "$produkt":"Samochód",
    "$cena":"20000",
    "$przedmiot":"Fizyki"
    }

napis = "Ten $produkt kosztuje $cena"
napis2 = "Zajecia z $przedmiot zostały odwołane"

def formatuj(napis,**co_na_co ):
    print(type(co_na_co))
    for klucz in co_na_co:
        napis=napis.replace("$"+klucz,co_na_co[klucz])
    print(napis)
    return napis
print(formatuj("Ten $produkt kosztuje $cena",**co_na_co))
print(formatuj("Zajecia z $przedmiot zostały odwołane",**co_na_co))

assert formatuj(napis, produkt="Samochod", cena="200000") == "Ten Samochod kosztuje 200000"
assert formatuj(napis2, przedmiot="Fizyki") == "Zajecia z Fizyki zostały odwołane"


def formatuj2(*napisy,**co_na_co ):
    wynik=[]
    for napis in napisy:
        for klucz in co_na_co:
            napis=napis.replace("$"+klucz,co_na_co[klucz])
        wynik.append(napis)
    if len(wynik)==0:
        return wynik[0]
    return napis
assert formatuj(napis,napis2,produkt="Samochod", cena="200000",przedmiot="Fizyki") ==["Ten Samochod kosztuje 200000","Zajecia z Fizyki zostały odwołane"]


#"\n".join(lista)