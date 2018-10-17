i = []

while len(i)<10:
    x=input("Podaj liczbę lub 'k; zeby zakonczyc: ")
    if x == "k":
        break
    liczba = int(x)
    i.append(liczba)

if len(i) == 0:
    print("Nie podano danych")
else:
    d = sum(i) / len(i)
print(f"Średnia wartosc to : {d}")