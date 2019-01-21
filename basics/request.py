from threading import Thread
from collections import namedtuple
from urllib.request import urlopen
from time import time


class MyThread(Thread):
    def run(self):
        with urlopen(f"https://www.metaweather.com/api/location/search/?query=Warsaw") as file:
            print(file.read())
poczatek = time()

watki = []
for i in range(100):
    watek = MyThread()
    watek.start()
    watki.append(watek)

for watek in watki:
    watek.join()

koniec = time()

total_time = koniec - poczatek

print(f"Czas: {total_time}s")



