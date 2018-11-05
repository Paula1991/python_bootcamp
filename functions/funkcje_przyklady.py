# def hello():
#     print("Hello world")
#     return 10
# def hello2(name):
#     print(f"Hello {name}")
#
# def hello3(name="World"):
#     print(f"Hello {name}")
#
# hello()
# hello2("Paulina")
#
# x = print("testuje co zwraca print")
# print("x",x)
# y= dir()
# print("y",y)
# z=hello()
# print("z",z)
#
def dodaj(a,b):
    return a + b
#  #   if b.isnumeric():
#
#     return a+b
#
# wynik = dodaj(10,11)
# wynik2=dodaj(1.1,20.2)
# wynik3=dodaj("a","b")
# print(wynik,wynik2,wynik3)

# def test_dodaj_dwie_liczby():
#     assert dodaj(1,2) == 3
#
# def test_dodaj_dwa_napisy():
#     assert dodaj("1","2") ==


def klon(imie,wiek=18,wzrost=165):
    print(f"Witaj {imie}")
    if wiek == 18 and wzrost ==165:
        print(f"Masz standardowe parametry")
    else:
        print(f"Roznisz sie od pozostalych")
        print("wiek",wiek)
        print("wzrost",wzrost)
klon("Adam",19)
klon("Paulina", wzrost=162, wiek=14)