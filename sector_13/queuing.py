''' QUEUING IN THREADS WITH SHARED STATE'''
# dont use threads for sequential task but
# if you want operations to happen sequentially using threads then you have to set up queuing system 

# you have queues so that your threads cannot interrupt one another

import time
import queue
import random
from threading import Thread

counter = 0
job_queue = queue.Queue() # things to be printed out
counter_queue = queue.Queue() # amounts by which to increase the counter

def increment_manager():
    global counter
    while True:
        increment = counter_queue.get() # this waits until an item is available and then locks the queue
        # no other thread can execute until task is done
        old_counter = counter
        counter = old_counter + increment
        job_queue.put((f"New counter value is {counter}", "-------"))
        counter_queue.task_done() # unlocks the queue now another thread could go back and get something

Thread(target = increment_manager, daemon = True).start() # this will continue forever until it finds error

def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()

Thread(target = printer_manager, daemon = True).start()

def increment_counter():
    counter_queue.put(1)

# worker threads

worker_threads = [Thread(target = increment_counter) for thread in range(10)]

for thread in worker_threads:
    thread.start()

for thread in worker_threads:
    thread.join()

counter_queue.join() # for them to get empty
job_queue.join()
