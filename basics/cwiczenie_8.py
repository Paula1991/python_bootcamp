liczba = input("dlugosc: ")
liczba2 = input("szerokosc: ")
liczba3 = input("wysokosc: ")

liczba = int(liczba)
liczba1 = int(liczba)
liczba2 = int(liczba)

objetosc = liczba * liczba1 * liczba2

if objetosc > 1000:
    print("Objętość większa niż 1 litr")
elif objetosc==1000:
    print("Objętość równa litrowi")
else :
    print("Objętość mniejsza niż litr")

a=2
# a  ,"",[],{},None są traktowane w if jako False
# 1,"A",[1,0],{1,2}, (1:2)
if a:
    print("Mam pewność,że a!=0")