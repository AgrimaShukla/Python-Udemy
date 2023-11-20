#  Do it again

#  we can use yield statement to receive data

def greet():
    friend = yield
    print(f"Hello, {friend}")

g = greet()
g.send(None) # priming the generator - it runs upto right before the yield
g.send("Adam") # this goes inside the yield then the function assigns Adam to friend

# doing multitasking

from collections import deque

friends = deque(("Rolf", "Jose", "Charlie"))

def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f"{greeting} {friend}")

def greet(g):               # this function can also be written as
    g.send(None)                # def greet(g):
    while True:                     #yield from g 
        greeting = yield             ''' from used to receive data and forward to another generator'''
        g.send(greeting)

greet_obj = greet(friend_upper())
greet_obj.send(None) # can also use next() here
greet_obj.send("Hello,")
print("Hello, multitasking..")
greet_obj.send("How are you?")

''' generators that receive data are no longer generators as they are not generating data,
they are receiving data so they are called co-routine because they take in data and can be suspended '''


'''
 generator-iterators begin execution at the top of the generator’s function body, there is no yield expression
 to receive a value when the generator has just been created. Therefore, calling send() with a non-None argument 
 is prohibited when the generator iterator has just started, and a TypeError is raised if this occurs (presumably due 
 to a logic error of some kind). Thus, before you can communicate with a coroutine you must first call next() or send(None)
   to advance its execution to the first yield expression.
'''

