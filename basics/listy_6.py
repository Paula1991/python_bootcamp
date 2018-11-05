liczby = [5,2,1,4,3]

min_ = liczby[0]
max_ = liczby[0]

for liczba in liczby:
    if liczba < min_:
        min_ = liczba
    if liczba > max_:
        max_= liczba

#liczby[liczby.index(min_)]=max_
#liczby[liczby.index(max_)]=min_


liczby[liczby.index(min_)] , liczby[liczby.index(max_)] = max_ , min_

print("Wartosci:" , min_ ,max_)
print("Indeksy, czyli pozycje:" , liczby.index(min_), liczby.index(max_))

#x = liczby[0]
#liczby[0] = liczby[2]
#liczby[2]=x

assert liczby == [1,2,3,4,5]