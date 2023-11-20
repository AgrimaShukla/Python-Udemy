# Asynchronous Python Development
'''
Synchronous: actions that happen one after another. Programming as we've seen it until now is synchronous, because each line executes after the previous one.
Asynchronous: actions that don't necessary happen after one another, or that can happen in arbitrary order ("without synchrony").
Concurrency: The ability of our programs to run things in different order every time the program runs, without affecting the final outcome.
Parallelism: Running two or more things at the same time.
Thread: A line of code execution that can run in one of your computer's cores.
Process: One of more threads and the resources they need (e.g. network connection, mouse pointer, hard drive access, or even the core(s) in which the thread(s) run).
GIL: A key, critical, important resource in any Python program. Only one is created per Python process, so it's unique in each.
'''

# Dining Philosophers


# Core - unit inside a computer that can perform some mathematical operations

'''
core is a processing unit of the CPU. It is responsible for executing programs and multiple
other actions on a computer

we can divide core into three parts
1) Control unit (CU) - it instructs the memory, logic unit and both i/p and o/p devices 
                       of the computer on how to respond to program's instructions
2) Arithmetic logic unit (ALU) - electronic circuit that execute arithmetic and logical operations
                                 
3) Memory - consists of registers and cache
'''

# Thread is a seperate execution path.
'''
It is a lightweight process that the operating system can schedule and run concurrently
with other threads
'''
" process does not run on the cores instead threads run on the cores"
# process is sort of a wrapper. A process contains at least one thread and some resources

# process contains one thread and the core the thread is running on

# IMP - threads run and process manages all the resources for its run

'''
waiting threads - for them there is time slicing

TIME SLICING 
- the OS has to save current status of the thread so that when it comes back to the core,
it doesn't start from the beginning
'''

# The Python GIL - global interpreter Lock
'''
When you launch Python app, you get a new Python process
means atleast one thread with it
in Python, you get one starting thread but you can make more

'''
# Parallelism not possible in python due to GIL
'''
Due to how python is implemented, you cannot run two threads in one process at the same time
each process in python creates a key resource
when a thread is running, it must acquire that resource
the resource - The GIL
'''

# MULTIPLE PYTHONS
'''
You can launch multiple python processes
Each process in python creates its own GIL
Each process creates one thread
But they cannot easily share data
'''

# cooperative multitasking
'''
- multiple tasks take turns running
- each task runs until it needs to wait for something, or until it decides it has run for long
- enough and should let another task run
reduce waiting time
'''

import time
from threading import Thread

def ask_user():
    start = time.time()
    user_input = input("Enter your name: ")
    greet = f"Hello, {user_input}"
    print(greet)
    print(f"ask user, {time.time() - start}")
 
def complex_calculation():
    start = time.time()
    print("Started calculating..")
    [x**2 for x in range(20000000)]
    print(f"complex calculation, {time.time() - start}")

start = time.time()
ask_user()
complex_calculation()
print(f"Single thread total time: {time.time() - start}")

# thread1 = Target(target, args) where target is the function to be executed whereas args is the arguments to be passed
thread1 = Thread(target = complex_calculation) # total 3 threads - thread1, thread2, and main thread
thread2 = Thread(target = ask_user)

start = time.time()
thread1.start()
thread2.start()
'''
here you can write something to kill the thread but you should not do that,
because the thread has acquired GIL and if it does not release the thread and we have
killed it that means GIL is gone
'''
# threads will not release the resources you have to release them manually
thread1.join() # this tells the main thread to wait until thread1 is finished
thread2.join() # join - blocking operation

print(f"Two thread total time: {time.time() - start}")


# to first create threads then assign targets to random threads
from concurrent.futures import ThreadPoolExecutor
# ThreadPoolExecutor creates a pool of thread with no target

with ThreadPoolExecutor(max_workers = 2) as pool: # max_worker = 2 means create two threads from pool of threads
    pool.submit(complex_calculation)
    pool.submit(ask_user)

# with statement - waits for the pool to finish
# if using with we don't have to use pool.shutdown()


# MULTIPROCESSING IN PYTHON

'''
A process gets created when we launch python app and we can ask python
code to launch another process
'''

# atomic operations are very important when you have shared state between the threads




import time
from multiprocessing import Process

def ask_user():
    start = time.time()
    user_input = input("Enter your name: ")
    greet = f"Hello, {user_input}"
    print(greet)
    print(f"ask user, {time.time() - start}")
 
def complex_calculation():
    start = time.time()
    print("Started calculating..")
    [x**2 for x in range(20000000)]
    print(f"complex calculation, {time.time() - start}")

start = time.time()
# ask_user()
# complex_calculation()
# print(f"Single thread total time: {time.time() - start}")

process = Process(target = complex_calculation)
process2 = Process(target = ask_user) # if here target is complex_calculation no error as multiprocessing which means two thing
# run at the same time in the CPU 

process.start()
process2.start()

start = time.time()

process.join()
process2.join()
print(f"Total time - {time.time() - start}")

'''
this whole code will throw an error - it cannot execute the input function because it does not have
access to the terminal as processes cannot share resources very easily also because the process are accessing
the console at the same time but they are separate entity
'''
print(f"Two process total time: {time.time() - start}")


'''
when the function is waiting (ask_user) we use multithreading otherwise we use multiprocessing
because in waiting we want to have cooperative multitasking between the two threads
'''

from concurrent.futures import ProcessPoolExecutor
# processpoolexecutor uses the no.of CPU cores for creating an optimized no of processes to create
with ProcessPoolExecutor(max_workers = 2) as pool:
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)



'''
if we want to reuse our process and bring it back to the pool of processes
we can do that without 'with'
'''