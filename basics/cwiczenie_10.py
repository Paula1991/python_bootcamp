#przyjecie argumentow
x = int(input("Podaj pierwszą liczbe: "))
y = int(input("Podaj druga liczbę: "))
operacja = input("Podaj rodzaj operacji: [+-*/] ")


#ify na operacje
if operacja == "+":
    wynik = x + y
elif operacja == "-":
    wynik = x - y
elif operacja == "*":
    wynik = x * y
elif operacja == "/":
    if y==0:
        wynik = "Nie dziel przez zero"
    else:
        wynik = x/y
else:
    print("zły operator")
print(f"Wynik działania {operacja} na argumentach: {x}, {y} to: {wynik}")