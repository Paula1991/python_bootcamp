Miasto_A = input("Miasto A: ")
Miasto_B = input("Miasto B: ")
dystans = int(input(f"Dystans {Miasto_A}-{Miasto_B}: "))
Cena_paliwa = float(input("Cena paliwa: "))
Spalanie = float( input("Spalanie na 100 km : "))
print()

koszt = (dystans /100)* Spalanie * Cena_paliwa
koszt = round(koszt, 2)
print(f"Koszt przejazdu Warszawa-Gdańsk {Miasto_A}-{Miasto_B} to {koszt}PLN")
