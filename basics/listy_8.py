napis = input("Podaj napis: ")


print(napis.index(">") - napis.index("<") - 1)


nawiasy="<>"
czy_zliczac = False
licznik=0

for i in napis:
    if i == "<":
        czy_zliczac = True
    elif i == ">":
        czy_zliczac = False
    elif czy_zliczac:
        licznik += 1

print(f"Liczba znaków w nawiasie : {licznik}")