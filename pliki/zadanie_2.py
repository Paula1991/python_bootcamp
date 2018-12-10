import sys

total_time={}
ostatnie_logowanie={}

def rozwiazanie_pierwsze:
    with open("dane/logs.txt") as f:
        for linia in f:
            user, akcja, czas = linia.split(";")
            czas=int(czas)
            if akcja == "LOGIN":
                ostatnie_logowanie[user]= czas
            elif akcja == "LOGOUT":
                total_time[user]= total_time.get(user,0) + czas - ostatnie_logowanie[user]


def rozwiazanie_drugie:
    total_time = {}
    ostatnie_logowanie = {}

    with open("dane/logs.txt") as f:
        for linia in f:
            user, akcja, czas = linia.split(";")
            czas = int(czas)
            if akcja == "LOGIN":
                total_time_login[user] = total_time_login.get(user,0) + czas
            elif akcja == "LOGOUT":
                total_time_logut[user] = total_time_logut.get(user, 0) + czas

    final_result= {}
    for user in total_time_login:
        final_result[user]= total_time_logout[user]-total_time_login[user]

def rozwiazanie_trzecie:
    out={}
    with open("dane/logs.txt") as f:
        for linia in f:
            user, akcja, time_str = linia.split(";")
            time = int(time_str)
        if akcja == "LOGIN":
            out[user] = out.get(user,0) - time
        if akcja == "LOGOUT":


print("Czas przebywania w systemie: ")
for user, czas in sorted(total_time.items() , key =nazwa , reverse=True)
print(f' {user}: {time} s')

