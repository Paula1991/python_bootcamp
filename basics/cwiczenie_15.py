from random import randint

graczX = randint(0,10)
graczY = randint(0,10)
skarbX = randint(0,10)
skarbY = randint(0,10)

while True:
    z = input("Podaj kierunek: ")

    print(f"Polozenie gracza to ({graczX},{graczY})")

    minKrokowPrzed= abs(skarbX-graczX) + abs(skarbY-graczY)

    if z == 'W':
        graczY += 1
    elif z == 'S':
        graczY-=1
    elif z == 'A':
        graczX-=1
    elif z == 'D':
        graczX+=1

    minKrokowPo = abs(skarbX-graczX) + abs(skarbY-graczY)

    if minKrokowPo == 0:
        print('Znalazles skarb')
        break
    if randint(1,5)< 5:
        if minKrokowPrzed < minKrokowPo:
            print("Oddalasz sie")
        else:
            print("zblizasz sie")


    if graczY > 10 or graczY < 1 or graczX > 10 or graczX < 1:
        print('gracz jest poza plansza')
        break