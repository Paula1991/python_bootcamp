from time import time

#czas jest liczony od 1 stycznia 1970 w sekundach

def czas(func):
    def wrapper(*arcgs,**kwargs):
        przed_wywolaniem = time()
        wynik = func(*arcgs,**kwargs)
        po_wywolaniu = time()
        print(f"Czas wywołania funkcji : {po_wywolaniu- przed_wywolaniem} s")
        return wynik
    return wrapper



def fib(x):
    if x <=1:
        return x
    return fib(x-1) + fib(x-2)

@czas
def funkcyjna(x):
    return fib(x)

print(funkcyjna(35))
