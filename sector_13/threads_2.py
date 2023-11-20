# multithreaded code with shared state at same time
import time
import random
from threading import Thread

counter = 0

def inc_counter():
    global counter
    time.sleep(random.random())
    counter += 1
    time.sleep(random.random())
    print(f"New counter value: {counter}")
    time.sleep(random.random())
    print("-------")

for x in range(10):
    t = Thread(target=inc_counter)
    time.sleep(random.random())
    t.start()

# adding rabdom sleeps between statements when doing multi threaded code is called fuzzing
# as threads are running