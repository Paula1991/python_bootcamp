import sys
import os

def tree(katalog, ile_wciec=0):
    zawartosc = list(os.scandir(katalog))
    for element in zawartosc:
        if element == zawartosc[-1]:
            print(ile_wciec * "┕   " , element.name , sep="")
        else:
            print(ile_wciec * "|   ", element.name, sep="")
        if element.is_dir():
            tree(element, ile_wciec +1)


directory=sys.argv[1]
tree(directory)
