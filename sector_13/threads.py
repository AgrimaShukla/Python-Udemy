from multiprocessing import Process
import time
import os

print("Upar se ")


def ask():
    start = time.time()
    name = input("Enter your name: ")
    greet = f"Hello {name}"
    print(greet)
    print(f"ask func took {time.time() - start}")


def run_long_2():
    start = time.time()
    print("Im from 2")
    for _ in range(200000000):
        continue
    print(f"run_long took {time.time() - start}")


def run_long_1():
    start = time.time()
    print("Im from 1")
    for _ in range(200000000):
        continue
    print(f"run_long took {time.time() - start}")


print(__name__)
print("pid: ", (os.getpid()))
if __name__ == "__main__":
    start = time.time()
    process1 = Process(target=run_long_1)
    process2 = Process(target=run_long_2)

    process1.start()
    process2.start()

print("Secret Key")