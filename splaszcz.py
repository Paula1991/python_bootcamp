lista=([1,2,3,[4,5,[6]],7])

#int, float, list, tuple,str,dict,set,complex
def splaszcz(lista):
    out = []
    for element in lista:
        if isinstance(element,list):
            out.extend(splaszcz(element))
        else:
            out.append(element)
    return out

def test_splaszcz():
    lista = [1,2,3,4,5]
    assert splaszcz(lista) ==[1,2,3,4,5]

def test_splaszcz_jedno_zagniezdzenie():
    lista = [1,[2,3]]
    assert splaszcz(lista) == [1,2,3]


 #           wynik=splaszcz(element)
#            for el in wynik:
 #               out.append(element)