# Advanced python development

# id is the address of the object in memory
# id function gives the first cell in the group because an object can take up multiple cells

my_int = 9
my_int += 1 # my_int.__iadd__(self, 1) as this creates new object wvery time means it is immutable

friends = {
    'Agrima': 21,
    'Anirudh': 16,
    'Nandini': 30
}

def new_friend(friends_age, name):
    print(id(friends_age)) # - prints same output as friend
    friends_age[name] = 20

print(id(friends))
new_friend(friends, 'Agrima')

# to compare two ids 'is' keyword is used

age = 20
def increase_age(current_age):
    current_age = current_age + 1

print(id(age)) # this gives the same id as in line 60
increase_age(age)
print(id(age))

primes = [2,3,4]
print(id(primes))

primes += [7,11]
print(id(primes)) # same id as above as __iadd__() is called because iadd modifies itself

primes = primes + [7,11]

print(id(primes)) # different id from above ad __add__() is called


def acc(name, holder, acc_holder = []):
    acc_holder.append(holder)   # the list will have same id everytime a function is called
    return name

a1 = acc('checking', 'Agrima')
a2 = acc('savongs', 'Shruti')

# we use * for tuples and ** for dictionaries
# study dictionary unpacking
def func(a,b,c,d):
    print(a,b,c,d)
my_list = [1,2,3,4]
func(my_list) # TypeError: func() takes 4 arguments 
func(*my_list)

# QUEUES
# A queue where you can add or remove things from either side is called a 'deque' or 'double-ended queue'


''' Collections Module '''
# counter - are unordered collection where elements are stored as dict keys and count as dict value

from collections import Counter

temp = [13.5, 14.0, 12.5, 15.0, 26.0]
temp_count = Counter(temp)
print(temp_count[2])

# defaultdict
'''
- it never raises a key error. It provides a default value for the key that does not exists
- it is a sub class that returns dictionary like object
'''
from collections import defaultdict
coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'), ('Charlie', 'Manchester')]

alma_maters = defaultdict(list)

for coworker, place in coworkers:
    alma_maters[coworker].append(place)

alma_maters.default_factory = None
print(alma_maters['Rolf']) # ['MIT', 'Cambridge']
print(alma_maters['Anne']) # []

my_company = 'apple'
coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Google'), ('Anna', 'Microsoft')]

coworker_companies = defaultdict(lambda: my_company)

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies[coworkers[0]]) # apple
print(coworker_companies['Rolf']) # google

# Ordered Dict - maintains order in which they were inserted not alphabetical or numerical

from collections import OrderedDict

o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3

print(o) # OrderedDict([('Rolf', 6), ('Jose', 12), ('Jen', 3)])

o.move_to_end('Rolf') # move to end
o.move_to_end('Jen', last = False) # move to start
o.popitem() # last item poped off

# namedtuple

from collections import namedtuple

account = ('checking', 1850.90)
print(account[0]) # name
print(account[1]) # balance

Account = namedtuple('Account1', ['name', 'balance'])
account = Account('checking', 1850.90)
accountNamedTuple = Account._make(account)
accountNamedTuple = Account(*account)
print(accountNamedTuple._asdict())

from collections import deque
friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
friends.append('Jose') 
friends.appendleft('Anthony')
print(friends) # deque(['Anthony', 'Rolf', 'Charlie', 'Jen', 'Anna', 'Jose'])

friends.popleft()
print(friends) # deque(['Rolf', 'Charlie', 'Jen', 'Anna', 'Jose'])


'''TIMEZONES'''
# UTC = Coordinated Universal Time

'''
Dates and times in Python
- A date and time object in python that does not know about timezones is called 'naive'
'''
from datetime import datetime
print(datetime.now()) # do not use this because it does not know about timezones

from datetime import datetime, timezone
print(datetime.now(timezone.utc))
# Arrow library

# module datetime with class datetime

from datetime import datetime, timezone, timedelta
print(datetime.now())
print(datetime.now(timezone.utc))

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days = 1) # used to calculate difference in dates
print(tomorrow)

print(today.strftime('%d-%m-%Y %H:%M')) # string format time - converts time input to string output

user_date = input("Enter the date in YYYY-mm-dd format: ")
user_date = datetime.strptime(user_date, '%Y-%m-%d') # string parse time - converts string input to time output


# timeit - simple way to find the execution time in small bits of Python code
'''
specially designed for measuring execution time of small code snippets
- provides a convenient way to repeadly time the execution of a piece of code
and gives best estimation
'''
import timeit
print(timeit.timeit("[x**2 for x in range(10)]"))


# REGULAR EXPRESSIONS - REGEX
'''
These are patterns used to match character combinations in string

Four most important components:
- '.' - dot - "anything" letters, numbers, symbols but not newlines
- '+' - "one or more of"
- '*' - "zero or more of"
- '?' - "zero or one of"
'''
import re
email = "abc@gmail.com"
exp = '[a-z]+'
matches = re.findall(exp, email)
print(matches) # ['abc', 'gmail', 'com']
name = matches[0]
domain = f"{matches[1]}{matches[2]}"

exp = '[a-z\.]+' # ['abc', 'gmail.com']

'''
re.search() - method either returns None (if the pattern doesn't match)
or a re.MatchObject that contains information about the matching part of the string
- This method stops after the first match
- suited for testing a regular expression more than extracting data
'''

'''
re.findall() - return all non-overlapping matches of pattern in string
             - a list of string
'''

price = 'Price: $189.50'
expression = 'Price: \$(189.50)' # included brackets # '([0-9]*\.[0-9]*)

matches = re.search(expression, price)
print(matches.group[0]) # entire match 
print(matches.group[1]) # first bracket , if no bracket then error


email = "abc@gmail.com"
exp = '[a-z]+'
matches = re.findall(exp, email)
print(type(matches))

# Introduction to logging in python
'''
Logging means tracking events that happen when some software runs
It has some levels of logging - you can disable
'''

import logging
logging.basicConfig(format = '%(asctime)s %(levelname)s:%(message)s', 
                    datefmt = '%d-%m-%Y %H:%M:%S',
                    level = logging.DEBUG,
                    filename = 'logs.txt') # minimum level you want to show # s stands for string
# for filename and line number [%(filename)s:%(lineno)d]
logger = logging.getLogger('test_logger')  # or instead of 'test_logger' use '__name__'
# this is meant to be used across multiple files
# if we call from different file then it is going to give same object

'''
Logging levels-
1) DEBUG - give detailed information 
2) INFO - used to confirm that things are working as expected
3) WARNING - indication that something unexpected happened or some problem in near future
4) ERROR - software has not been able to perform some function
5) CRITICAL - serious error
'''
logger.info('This will not show') # don't show up by default

# gives stack trace

logging.basicConfig(level = logging.INFO, filename = "log.log", filemode = "w",
                    format = "%(asctime)s - %(levelname)s - %(message)s")

try:
    1 / 0
except ZeroDivisionError:
    logging.exception("ZeroDivisionError")

# HIGHER ORDER FUNCTIONS - accept other functions as parameters and run them inside their own body
def greet():
    print("Hello")

def before_and_after(func):
    print('Before')
    print(func())
    print('After')

before_and_after(lambda: 5)
before_and_after(greet) # greet() - not like this as this will call the function and it will return none and none witll be passed



movies = [
    {"name": "YJHD", "director": "Ayan"},
    {"name": "ZNMD", "director": "Zoya Akhtar"}]

def find_movie(looking, func):
    for movie in movies:
        if looking == func(movie):
            return movie
      


find_by = input("What property are we searching? ")
looking = input("What are you looking for? ")
print(find_movie(looking, lambda movie: movie[find_by]))

# study itertools from section end
