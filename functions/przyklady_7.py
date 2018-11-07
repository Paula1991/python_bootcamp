lista=[1,2,3,4,5,6]


#waruek jest taki, że większe niż 3
out=[False,False,False,True,True,True]


def bigger_than_3(liczba):
    if liczba>3:
        return True
    else:
        return False
def smaller_than_3(liczba):
    if liczba<3:
        return True
    return False
def czy_rowne_4(argument):
    if argument==4:
        return True
    return False


x = lambda i:i ==4
def x(i):
    if i ==4:
        return True
    return False

def sprawdzam_czy(lista,warunek):
    out=[]
    for element in lista:
        # if element>3
        #     out.append(True)
        # else:
        #     out.append(False)
        out.append(warunek(element))
    return out

# def sprawdzam_czy(lista,warunek):



assert sprawdzam_czy(lista, bigger_than_3) == out
assert sprawdzam_czy(lista, czy_rowne_4) == [False,False,False,True,False,False]
assert sprawdzam_czy(lista, warunek= lambda x:x ==4)==[False,False,False,True,False,False]



