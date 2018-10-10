suma_temperatur=0
i=0
while i<7:
    dane = input("Podaj temperatue lub wpisz k by zakonczyc: ")

    if dane=="k":
        break
    suma_temperatur+=float(dane)
    i+=1

print("Średnia temperatura to : " , round (suma_temperatur/i,2))