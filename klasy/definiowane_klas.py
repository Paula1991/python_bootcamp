

class Animal:
    krolestwo = "Fauna" #atrybut klasowy
    def __int__(self,nazwa):
        self.nazwa=nazwa

#main nazwa pliku z wnetrza



a1 =Animal("zyrafa") #instancja klasy
a2=Animal("mysz") #instancja klasy

print(a1.krolestwo)
print(a1.krolestwo)

print(a1.nazwa)
print(a2.nazwa)
#print(type(zyrafa.krolestwo))

Animal.krolestwo ="Flora"

zyrafa.krolestwo = "Fauna"
print(zyrafa.krolestwo)
print(mysz.krolestwo)