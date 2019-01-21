def wypisz_samogloski(napis):
    for i in napis:
        if i in "aeiouy":
            yield i

def generator(napis):
    for i in napis:
        yield i

x = input("Podaj napis: ")

for char in wypisz_samogloski(x):
    print(char)
