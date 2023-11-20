# Destructuring
fmt = [("Agrima", 24), ("Niyati", 25)]

for name, age in fmt:
    print(f"My name is {name} and age is {age}")

fmt = {"Rolf": 25, "Bob": 26}
for name in fmt:
    print(name) # Agrima, Niyati

for ages in fmt.values():
    print(ages)


# else can be used with for and while loop
for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break")

# prime numbers
for i in range(2, 10): 
    for j in range(2, i):
        if i%j == 0:
            print(f"{i} equals {j} * {i//j}")
            break
    else:
          print("Prime")

# Last slicing
friends = ["Agrima", "Meghna", "Shruti"]
print(friends[-1:0])

# List comprehension
numbers = [1,2,3,4,5]
doubled = [n * 2 for n in numbers]

# Set comprehension
friends = ["Agrima", "Shruti", "Meghna"]
family = ["Agrima", "Yashasvi", "Advaita"]

lower_friends = {n.lower() for n in friends}
lower_family = {m.lower() for m in family}

inter = lower_friends.intersection(lower_family)
list1 = [inter.name()]

# Dictionary comprehension
friends = ["Agrima", "Mahak", "Niyati"]
age = [21, 22, 20]

friends_age = {
    friends[i]: age[i] # Maps ith index of friends with ith index of age
    for i in range(len(friends))
}
print(friends_age)


# Zip function - takes iterable containers and returns a single iterator object
# Zip - Two iterables into tuple
# If no of the elements do not match, zip will ignore the elements that don't the match the other list
list1 = ["Abhishree", "Anegha", "Dhairya"]
list2 = [23, 34, 25]

for name, age in zip(list1, list2):
    print(f"Name is {name} and age is {age}")

list3 = dict(zip(list1, list2))

# enumerate() function takes a collection and returns it as an enumerate object
# enumerate() adds a counter as the key of the enumerate object
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(list(y)) # = print(list(zip([0,1,2], x)))
print(dict(y))

y = enumerate(x, start=1)

# function
def greet():
    print("Hello")

greet()

# Argument - value you pass into the function
# Parameter - variable that accepts a value inside a function

def car_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon")

car_mpg({
    "make": "Ford",
    "model": "Fiesta",
    "mileage": 2300,
    "fuel_consumed": 460
})

# List of dictionaries
cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel": 360}
]
car_mpg(cars[1])

# functions
def car_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon")

'''car_mpg(
    {"make": "Ford",
    "model": "Fiesta",
    "mileage": 2300,
    "fuel_consumed": 460})
'''
cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 360}
]

for car in cars:
    car_mpg(car)

# Return statement
for car in cars:
    name, mpg = car_mpg(car)
    print(f"{name} has {mpg}")

# default parameter values
def add(x, y = 3): # here the value of y =  3 will be overwritten by value 6 
    z = x + y
    print(z)

add(5, 6) # can also write as add(x = 5) --> this is called NAMED ARGUMENTS
add(5, y=2) # ERROR - as an argument which does not have a name can be passed after the value which has a name

def sub(x , y=9): # ERROR - dafault values goes at the end, if one parameter has a default value
    z = x - y       # then all the subsequent parameters must have default values
    print(z)

sub( y=6)
    
# sep - separator between the arguments to print() function
print(1, 2, 3, sep = '-') # output = 1-2-3

#
default_y = 3
def add(x, y = default_y):
    total = x + y
    print(total)

add(2) # output - 5
default_y = 5
add(2) # output - 5 as the default value of will not change, this is highly discouraged
add(2, 5) # here y value changes to 5

# lambda function
# It is used to define an anonymous function in python- a function without a name
# this function can have any no of arguments but only one expression
# can provide more simplicity to code
# are used for giving inputs and returning outputs but are not used for performing actions

divide = lambda x, y: x/y
print(divide(15, 3))

# another way to call lambda function
print((lambda x, y: x / y)(15, 3)) # not used much

average = lambda seq: sum(seq) / len(seq)
students = [
    {"name": "Agrima", "grades": (99, 98, 97, 65)},
    {"name": "Shruti", "grades": (87, 89, 99, 92)}
]
for student in students:
    print(average(student["grades"]))


# first class function - we can assign functions to variables and we can pass them as arguments to other functions
# both named and lambda functions are first class functions
def greet():
    print("Hello")

hello = greet
hello()


# to create associations in python use dictionaries
students = [
    {"name": "Agrima", "grades": (99, 98, 97, 65)},
    {"name": "Shruti", "grades": (87, 89, 99, 92)}
]

avg = lambda av: sum(av) / len(av)
total = lambda tot: sum(tot)
top =  lambda sum1: max(sum1)

operations = {
    "average": avg,
    "sum": total,
    "max": top 

}
for student in students:
    name = student["name"]
    grades = student["grades"]

operator = input("Enter any one: average, max or sum: ")

operation_func = operations[operator]
print(operation_func(grades))
