''' before as we were implementing threads there was a task scheduler at the background the OS
bringing threads to the core and removing them'''

# using generators to achieve multitasking (multitasking - looks things happening at same time but are actually not)

def countdown(n):
    while n > 0:
        yield n
        n -= 1

tasks = [countdown(10), countdown(5), countdown(20)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Finished')


''' if a task takes a long time to run then we can offload that to separate thread or separate process 
then we can use threadpoolexecutor or processpoolexecutor'''
