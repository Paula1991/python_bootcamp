liczby = set()

while True:
    tekst = input("Wprowadź liczbę lub k by zakończyć: ")
    if tekst.lower() == 'k':
        break
    else:
        liczba = int(tekst)
        liczby.add(liczba)
print(f"Unikalnych liczb: {len(liczby)}")
liczby_parzyste =set(range(2, 101, 2 ))
print(f"W tym liczb parzystych od 0 do 100 {len(liczby & liczby_parzyste)}")