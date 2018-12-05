import sys

total_time={}
ostatnie_logowanie={}

with open("dane/logs.txt") as f:
    for linia in f:
        user, akcja, czas = linia.split(";")
        czas=int(czas)
        if akcja == "LOGIN":
            ostatnie_logowanie[user]= czas
        elif akcja == "LOGOUT":
            total_time[user]= total_time.get(user,0) + czas - ostatnie_logowanie[user]

print(total_time)


gi
