lista_produktow ={"pomidory":2, "ogórki":4,"ziemniaki":2,"cebula":1,"marchew":2}

magazyn={"pomidory":10, "ogórki":10,"ziemniaki":10,"cebula":10,"marchew":10}
koszyk={}

while True:
    komenda = input("""Wybierz opcje:
    [d] - dodaj do magazynu
    [k] - kup
    [z] zakoncz """)
    if komenda == "k":...
    elif komenda=="d":
        co = input("Jaki produkt chcesz dodac? ")
        ile = int(input(f"Ile {co} chcesz dodac?"))
        magazyn[co]= magazyn.get[co,0] + ile
        if co not in lista_produktow:
            cena = float(input(f"Jaka cena za {co}"))
            lista_produktow[co]=cena
    elif komenda == "z":
        break

print()
print()
print(f"Zaplacisz: ")
sumarycznie = 0
for nazwa_produktu in koszyk:
    print(f" - {nazwa_produktu}: {koszyk[nazwa_produktu]} PLN")
    sumarycznie += koszyk[nazwa_produktu]

print("=" * 30)
print(f"Suma: {sumarycznie} PLN")
print(f"Dziękujemy! Zapraszamy ponownie")
print("W naszym sklepie oferujemy: ")

for produkt in lista_produktow:
    print(f" - {produkt} - w cenie {lista_produktow[produkt]} PLN")

print()
nazwa_produktu = input(f"Podaj nazwę produktu lub zakończ żeby zakonczyc: ")
    if nazwa_produktu == "zakoncz":
        break
if nazwa_produktu in lista_produktow:
    waga = input(f"Ile chce kupić:[{nazwa_produktu}:] ")
    if waga <= magazyn[lista_produktow]:
        koszyk[nazwa_produktu] = naleznosc
        magazyn[nazwa_produktu]-= naleznosc
    else:
        print(f"Przykro mi. Nie mam tego produktu! Pozostało {magazyn}")
else:
    print(f"Sorry nie mam takiego produktu")
print()
print("-"*40)

print()
print()
print(f"Zaplacisz: ")
sumarycznie = 0
for nazwa_produktu in koszyk:
    print(f" - {nazwa_produktu}: {koszyk[nazwa_produktu]} PLN")
    sumarycznie += koszyk[nazwa_produktu]

print("="*30)
print(f"Suma: {sumarycznie} PLN")
print(f"Dziękujemy! Zapraszamy ponownie")
