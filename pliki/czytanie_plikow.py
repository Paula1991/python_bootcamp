
#otworzenie pliku do odczytu
with open("input.txt") as f: #context manager
    for linia in f:
        if len(linia) >600:
            print(linia)




# tryb do odczytu

with open("info.txt","w", encoding='utf-8') as f:
    for i in range(10):
        f.write("Jakiś tekst\n")

with open("info.txt", "a", encoding='utf-8') as f:
    f.write("inny tekst")


