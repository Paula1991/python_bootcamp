from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self):
        super().__init__()
        pass
        super().__init__()
        pass

    def run(self):
        sleep(4)
        print("czesc")

watek = MyThread()
watek.start()

print("Hej")