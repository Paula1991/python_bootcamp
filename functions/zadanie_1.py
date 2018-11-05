
# pustki =[0, None, "",[],(),set(),{}]
# assert pustki[1]
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# AssertionError
def czy_pierwsza(a):

    for x in range(2,a-1):
        if a%x==0:
            return False


    return True

def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert czy_pierwsza(101)
    assert czy_pierwsza(3)
    assert czy_pierwsza(11)

def test_czy_jest_pierwsza_dla_liczby_nie_pierwszej():
    assert not czy_pierwsza(121)
    assert not czy_pierwsza(10)
    assert not czy_pierwsza(81)

