zmienna_max = None
zmienna_min = None

while True:
    liczba = input("Podaj liczbę: "  )

    if liczba == "koniec":
        break

    x = int(liczba)
    if zmienna_max is None or x > zmienna_max:
        zmienna_max = x
    if zmienna_min is None or x > zmienna_max:
        zmienna_min = x

if zmienna_max is None:
    print("Nie wprowadzono danych")
else:
    print(f"max: {zmienna_max} min: {zmienna_min}")
