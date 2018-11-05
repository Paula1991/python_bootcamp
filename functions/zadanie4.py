def formatuj(*args, **kwargs):
    tekst = "\n".join(args)
    for klucz in kwargs:
        tekst=tekst.replace("$"+klucz,str(kwargs[klucz]))
    return tekst

def test_formatuj():
    assert formatuj (
        "koszt $cena PLN",
        "koszt $cena brutto",
        cena=10
    ) == 'koszt 10PLN\nkwota 10 brutto'

#parametry={"end":"Koniec", "sep":"_odstep_"}


#print("To jest pierwszy tekst", "To jest drugi tekst", **parametry)
#print("To jest trzeci tekst z osobnego printa")