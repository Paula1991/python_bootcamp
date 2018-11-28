lista = [1,2,3,4]

try:
    print(lista[3])
    lista.add(5)
    lista.append(5)
    print(lista)
except IndexError as e:
    print("probujeszcz pobrac jakis element spoza zakresu listy")
    raise IndexError("")
except AttributeError as e:
    print ("Prawdopodobnie wywolujesz metode, ktorej ten obiekt nie ma")


# except Exception as e:
# #     print("Wystapil jakis blad")
# #     print(e)