import sys

try:
    print(sys.argv[1])
except IndexError:
    print("zapomniales podac nazwe pliku")
print(sys.argv)
print("sciezka do pliku to:" , sys.argv[1])

with open(sys.argv[1]) as f:
    i=0
    for linia in f:
        print(i,linia)
        i +=1

