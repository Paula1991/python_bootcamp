# def fun():
#     print("Cześć")



# def prosty_prawie_dekorator(func):
#     def wrapper():
#         print("Przed wywołaniem")
#         func()
#         print("Po wywołaniu")
#     return wrapper
#
# fun= prosty_prawie_dekorator(fun)

def prosty_dekorator(func):
    def wrapper(*args,**kwargs):
        print("Przed wywołaniem")
        results =func(*args, **kwargs)
        print("Po wywołaniu")
        return results
    return wrapper

def dwa_wywolania(func):
    def wrapper(*args,**kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

# fun = dwa_wywolania(fun)
@prosty_dekorator
@dwa_wywolania
@dwa_wywolania
def fun():
    print("Cześć")


# @prosty_dekorator
#
# def fun():
#     print("Cześć")
#
# @prosty_dekorator
# def silnia(x):
#     print("Uwaga licze silnie")
#     wynik=1
#     for i in range(1,x+1):
#         wynik *=i
#     return wynik
#
print("Akuku")
fun()
# print(silnia(5))