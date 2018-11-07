
def rekurencja_print(n):
    if n ==0:
        return 1
    else:
        return n * silnia(n - 1)

def silnia_dla_0():
    assert silnia(0) == 1


def silnia_dla_wiekszych_od_0():
    assert silnia(2) == 2
    assert silnia(5) == 120
