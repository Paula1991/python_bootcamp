
# def wiecej_niz(napis,liczba_razy):
#     return set()

def wiecej_niz(napis,prog):
    for litera in napis:
        if napis.count(litera)>prog:
            wynik.add(litera)
    return set()


x=wiecej_niz("",0)
print(x)
#     napis = input("Podaj napis: ")
#     liczba_razy = input("Podaj liczbe razy: ")
#     if napis!="" and liczba_razy!=0:
#         return False
#     # while True:
#     #
#     #     if count(napis) > liczba_razy:
#     #     return True
#
def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("",0)==set()

def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz("aaa bb mc",2)=={'a'}
    assert wiecej_niz("aaa bb mc", 3) == set()