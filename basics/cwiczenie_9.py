import datetime
print(datetime.datetime.now())

year = datetime.datetime.now().year
rokurodzenia = int(input("Podaj rok urodzenia: "))

if year-rokurodzenia > 18:
    print("Jesteś pełnoletni!")
else:
    print("Jesteś niepełnoletni!")