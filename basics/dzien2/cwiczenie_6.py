liczba = input("Podaj liczbę: ")

liczba = int(liczba)
print(f"Większa od 10: {liczba>10}")
print(f"Mniejsza równa 15: {liczba <=15}")
print(f"Podzielna przez 2: {liczba%2 == 0}")
print(f"Podzielna przez 3 i większa od 10: {liczba%3 == 0 and liczba>10}")
print(f"Większa od 10 lub podzielona przez 5: {liczba>10  or liczba%5 ==0}")