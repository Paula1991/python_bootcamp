x = int(input("Podaj pozycję gracza X: "))
y = int(input("Podaj pozycję gracza Y: "))

if x>100 or y>100 or x<0 and y <0:
    pozycja= "Gracz jest poza plansza"
elif y>=90 and x<=10:
    pozycja = "lewy górny róg"
elif y>=90 and x>=90:
    pozycja ="prawy górny róg"
elif x<=10 and y<=10:
    pozycja ="lewy dolny róg"
elif y<=10 and x>=90:
    pozycja ="prawy dolny róg"
elif 10<y<90 and x<=10:
    pozycja ="lewa krawedz"
elif 10<y<90 and 90<=x:
    pozycja="prawa krawedz"
elif y>=90 and 10<x<90:
    pozycja="górna krawedz"
elif y<=10 and 10<x<90:
    pozycja="dolna krawędz"
else:
    pozycja="centrum"
print(f"Twoja pozycja to: {pozycja}")