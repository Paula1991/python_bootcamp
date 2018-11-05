liczby = [5, 2, 1, 4, 3]

print("Liczby przed: " , liczby)

for indeks_podstawienia in range(len(liczby)):
    index_minimum = indeks_podstawienia
    for indeks_ogona in range(indeks_podstawienia + 1, len(liczby)):
        if liczby[indeks_ogona] <liczby[index_minimum]:
            index_minimum = indeks_ogona
        value_temp=liczby[index_minimum]
        liczby[index_minimum]=liczby[indeks_podstawienia]
        liczby[indeks_podstawienia] = value_temp
      # liczby[index_minimum], lista[indeks_podstawienia=lista[indeks_podstawienia,liczby[index_minimum]

print("Liczby Po: " , liczby)
assert liczby ==(1,2,3,4,5)