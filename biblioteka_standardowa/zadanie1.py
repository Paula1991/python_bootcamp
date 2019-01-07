import json

# obiekt = {"imie": "Jan", "wiek":33}
#
# print((json.dumps(obiekt)))
#
# napis ='{"imie": "Jan", "wiek":33}'
#
# print(type(json.loads(napis)))

try:
    with open("pracownicy.json","r") as plik:
        pracownicy =json.load(plik)
except FileNotFoundError:
    pracownicy=[]

op= input("Co chcesz zrobic? [d-dodaj], [w-wypisz]: ")
if op == 'd':
    imie = input("Imie: ")
    nazwisko = input("Nazwisko: ")
    rok_urodzenia = int(input("Rok urodzenia: "))
    pensja = float(input("Pensja: "))

    pracownik={"Imię":imie, "Nazwisko":nazwisko,"Rok urodzenia":rok_urodzenia,"Pensja":pensja}
    pracownicy.append(pracownik)
    with open("pracownicy.json", "w") as plik:
        json.dump(pracownicy,plik)
elif op =="w":
    for nr,p in enumerate(pracownicy,1):
        print(f"- [{nr}] {p['imie']} {p['nazwisko']} - rok: {p['rok_urodzenia']}, pensja: {p['pensja']} PLN")