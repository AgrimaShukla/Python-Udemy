# in order to get rid of "yield from " we cam with "await" keyword

# coroutines
'''
coroutines in Python are a type of function hat can be pause their execution and allow
other code to run and then later resume where they left off.
'''
from collections import deque
from types import coroutine
friends = deque(("Agrima", "Shruti", "Meghna"))

@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f"{greeting} {friend}")

async def greet(g):
    print("Starting")
    await g # waits for friend_upper to finish but you can suspend in the middle
    print("Ending")

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
greeter.send("How are you")

''' output will be Starting then Hello AGRIMA and then How are you SHRUTI
but ending does not get printed out because we have not finished running the coroutine 
because coroutine has a loop and it continues running until friends is empty'''