# multiprocessing
from multiprocessing import Process
import time

def task(name):
    print(f"{name} start")
    time.sleep(2)
    print(f"{name} end")

if __name__ == "__main__":
    p1 = Process(target=task, args=("A",))
    p2 = Process(target=task, args=("B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")
