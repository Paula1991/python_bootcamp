def foo(pierwszy , *reszta ):
    #print("pierwszy",pierwszy)
    #rint("reszta",reszta)
    if reszta:
        return pierwszy + reszta[-1]
    return pierwszy

print(foo(1))

print(foo(1,2,3))

print(foo(1,2,5,10,15))

reszta = [1,2,5,"cos tam jeszcze"]
print(reszta)
print(*reszta)


def druga_funkcja(**slownik):
    if 'd' in slownik:
        return slownik['a'] + slownik['d']
    if slownik:
        return slownik['a']
    return "Żaden warunek nie był spełniony"

print('a' ,druga_funkcja())
print('a i d' , druga_funkcja(a=2,b=2,c=3,d=4))
print('a i d drugi raz', druga_funkcja(a=2,b=2,c=3,d=4, zosia=5,adas=15))
print('a dugi raz ale bez d', druga_funkcja(a=2,b=2,c=3,zosia=5,adas=15))





