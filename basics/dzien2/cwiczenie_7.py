liczba = input("Podaj liczbę: ")

liczba = int(liczba)
wynik = liczba == 7 or (liczba%2 == 0 and
                        liczba%3  == 0 and
                        liczba>10)

print(f"Liczba jest podzielna przez 2, podzielna przez 3 i większa od 10 lub to jest liczba 7: {wynik}")