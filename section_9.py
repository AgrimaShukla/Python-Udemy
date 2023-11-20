# Advanced built-in functions in python

# Generators function - remembers  the state it's in between executions
'''
- It gives first element of list, without storing rest in memory
- It allows you to declare a function that behaves like an iterator
- never stores list in memory only remember last element it gave you
- you have to run the function everytime you want a new number
- instead of return we write yield
- yield is used to produce a value from the generator
- when the generator is called, it does not execute the function body immediately
  instead, it returns a generator object that can be iterated over to produce the values
- also useful for running functions temporarily
'''

# Generators are useful when we want to produce a large sequence of values
# but we don't want to store all of them in memory at once

def hundred_num():
    i = 0
    while i < 100:
        yield i
        i += 1

g = hundred_num()
print(next(g)) # - 0 # next - returns the next item in an iterator
print(next(g)) # - 1
print(list(g)) # [2.....100]


# Generator class

class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self): # next(object)
        if self.number < 100:
            current =  self.number
            self.number += 1
            return current
        else:
            raise StopIteration()
        

my_gen = FirstHundredGenerator()
print(next(my_gen))

# ITERATORS - are those objects which have a dunder next method and we can call next in them

'''
ITERATOR VS ITERABLE

Iterable - an object that can iterate over. Generates an iterator when passed to iter()
Iterator - an object used to iterate over an iterable object using __next_()
           an iterator object must implement two special methods, __iter()__ and __next__()


For eg - list is an iterable but not iterator

'''
# All generators as iterators
# An iterator can be created from an iterable using the function iter()

# ITERABLE

'''
An iterable has an __iter__() method or an object which have len and getitem
- once we define this method in an object that means it is an iterable
- iter() used to convert an iterable to the iterator
'''

# Generator comprehension

my_numbers_gen = (x for x in [1,2,3,4,5])

print(next(my_numbers_gen))



# filter() in python
'''
The filter() method filters the given sequence with the help of a function that tests each element
in the sequence to be true or not

filter(function, sequence)
'''


def starts_with_r(friend):
    return friend.startswith('R')

friend = ['Rolf', 'Jose', 'Randy', 'Anna']
starts_with_r = filter(starts_with_r, friend) # filter(lambda friend: friend.startswith('R'), friends)

# filter returns a generator
print(next(starts_with_r))
print(list(starts_with_r))
# generator comprehension of above example

another_starts_with_r = (f for f in friend if f.startswith('R'))

# map(function, iterable) function
'''
- takes an iterable
- returns a new iterable where each element is modified according to some function
'''

'''
MAP VS FILTER

- MAP - takes all objects in a list and allows you to apply a function to it
- FILTER - takes all objects in a list and runs through a function to create a new list with all objects that return true in
 that function
'''

friends = map(lambda fren: fren.lower(), friend)



# ANY VS ALL
'''
ANY - returns true if any of its elements evaluate to true
ALL - returns true if all of its elements evaluate to true
'''

# bool(0) - False
print([1,2,3,4]) # - True
print([0, 1, 2, 3]) # - False
 