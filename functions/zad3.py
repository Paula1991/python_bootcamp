
def policz_znaki(napis,start="<", stop =">"):
    wynik=0
    poziom_zagniezdzenia=0
    for litera in napis:
        if litera == start:
            poziom_zagniezdzenia += 1
        elif litera == stop:
            poziom_zagniezdzenia -= 1
        else:
            wynik += poziom_zagniezdzenia
    return wynik


def test_policz_znaki_bez_znacznikow():
    assert policz_znaki('ala ma kota a kot ma ale')==0

def test_policz_znaki_jeden_poziom_zagniezdzenia():
    assert policz_znaki('ala ma <kota> a kot ma ale')==4


#def test_policz_znaki_wiele_poziomow_zagniezdzenia_niestandardowe_znaczniki():
 #   assert policz_znaki('ala [kota [a kot]] ma [ale]','[',']')==18
  #  assert policz_znaki('ala [kota;a kot]] ma [ale]', start='[',end=']') ==18

#def test_policz_znaki_standardowe_znaczniki_wiele_poziomow():
    #assert policz_znaki ('a <<a<>>>')==6

print(policz_znaki("Ala ma <kota>"))