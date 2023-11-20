# ERRORS

''' Errors are the problems in a program due to which the program will stop the execution
    Exceptions are raised when some internal events occur which changes the normal flow of the program

    Two type os errors
    1) Syntax errors 
    2) Logical errors (Exception)
'''

'''
TRACEBACK
Report containing the function calls made in your code at a specific point. 
Whenever the code gets an exception, the traceback will give the information about 
what went wrong in the code.

When a python program has a mistake, the interpreter can create a traceback that provides a 
series of function calls that went wrong and led to an error.
'''

# Stack traces
# A stack trace is used to display all the function calls before an error occurs.
# The error is reported at the final line of the stack trace 

'''
How to solve your errors-
1) Examine your code
2) Search your error message into google
3) Again look at your code slowly
4) Run only some parts of the code
5) Use a debugger
'''

'''
BUILT-IN ERRORS
1) IndexError - accessing an index that doesn't exist. List index out of range
2) KeyError - when we try to access a key from dictionary which doesn't exist
3) NameError - when variable not defined
4) AttributeError - when an attribute reference or assignment fails, when we deal with objects.  Eg - when we want to
                     take intersection of two lists('list' object does not have attribute 'intersection') but that only happens in sets and suppose 
                     we want to append second value in a variable.
5) NotImplementedError - Exception derived from RuntimeError. When a function is called but not implemented.
6) RuntimeError - base error and other errors inherit from this. Error that we encounter during the code execution during runtime. Eg - division by zero.
7) SyntaxError - invalid syntax
8) IndentationError 
9) TabError - inconsistent use of tabs and spaces in indentation.
10) TypeError - operation performed on an unsupported object type. Using + on a string and integer.
11) ValueError - correct argument but incorrect value to a function. Eg - converting an string to int which is valid but string is '11.2' which is a float 
                  or a negative number passed to a square root operation. 
12) ImportError - circular imports - importing one file which imports the same file (file a imports file b and file b imports file a
13) DeprecarionWarning - Warning not an error. Warnings that indicate the use of of a library or feature is suspended and no longer 
                         considered to be safe to use.           
'''
# Not Implemented Error - 
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        raise NotImplementedError('This feature has not been implemented yet') # when login method not implemented yet

# Value Error
str = '11.4'
val = int(str)
print(val)   # invalid literal for int() with base 10: '11.4'

# Raise Errors
# The raise keyword raises an error and stops the control flow of the program.
class Car:
    def __init__(self, make, model):
        self.make =  make
        self.model = model

    def __repr__(self):
        return f"<Car {self.make} {self.model}"
        
class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"Tried to add a {car.__class__.__name__} to the garage, but you can only add 'Car' objects. ") 
        self.cars.append('Ford')
    
ford = Garage()
ford.add_car('Fiesta') # TypeError: Tried to add a str to the garage, but you can only add 'Car' objects. 
car = Car('Ford', 'Fiesta')
ford.add_car(car)
print(len(ford))

# Inheriting from an error class
class MyCustomError(TypeError):
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code

#raise MyCustomError('Error Raised', 500)

# Docstrings
'''
- Short for documentation strings
- Convey the purpose and functionality of Python functions, modules and classes.
- It is specified in source code that is used, like a comment, to document a specific segment of code
- Declared using triple single quotes or triple double quotes.
- Can be accessed using __doc__ method'''

class Student:
    """Docstring"""
    def __init__(self) -> None:
        pass
    def my_func1():
        return None
    
print(Student.__doc__)

class MyCustomError(TypeError):
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code

err = MyCustomError("Error raised", 500)
print(err.__doc__)


# Try and except
'''
- It is used to handle errors within our code
- Try - lets you test a block of code for errors. Try block will execute when no errors found.
- Except - lets you handle the error. Except block will execute when errors found.
- Finally - lets you execute code, regardless of the result of the try and except blocks.
'''
class Car:
    def __init__(self, name):
        self.name = name

class Garage:
    def __init__(self, name):
        self.name = name
        self.make = []


    def add_car(self, name):
        if not isinstance(name, Car):
           raise TypeError(f"Raised") # Not will be printed because
        self.make.append(name)
        #print("Appended")

    def __len__(self):
        return len(self.make)
    

ford = Garage('Ford')
fiesta = Car('Fiesta')

try:
    ford.add_car(ford)

except TypeError:
    print("Your car was not of type car")

except ValueError:
    print("Value Error")

finally: # Will always execute
    print(f"Garage has {len(ford)} cars")

 

class User:
    def __init__(self, name, metrics):
        self.name = name
        self.data_metrics = metrics

def get_user_Score(user):
    try:
        return perform_calculation(user.data_metrics)
    except KeyError:
        print("Incorrect values provided")
        raise # shows the stack trace

def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2

my_user = User('Agrima', {'click': 51, 'hits': 100}) # error as 'click' written instead of clicks
print(get_user_Score(my_user))

''' To print a message when error not raised we can use else after except but try should not return anything because then 
the code will not further be executed

From above code:
'''
class User:
    def __init__(self, name, metrics):
        self.name = name
        self.data_metrics = metrics
        self.score = 0

def get_user_Score(user):
    try:
        user.score = perform_calculation(user.data_metrics)
    except KeyError:
        print("Incorrect values provided")
        raise
    else:
        if user.score > 500:
           send_notification(user)

def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2

def send_notification(user):
    print(f"Notification send to {user.name}")

my_user = User('Agrima', {'clicks': 51, 'hits': 100})
get_user_Score(my_user)
