napis = input("Podaj napis: ")

SAMOGLOSKI = "aeiouy"
licznik = 0
for l in napis.lower():
    if l in SAMOGLOSKI:
        licznik += 1
print(f"W napisie jest :  {licznik} samogłosek")




#print(napis[0])
#print("a" in napis)
#print("A" in napis)
