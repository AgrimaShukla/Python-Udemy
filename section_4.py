# OBJECT ORIENTED PROGRAMMING

''' EVERYTHING IN PYTHON IS AN OBJECT'''
# Class -
# user defined data type - which holds its own data members and member functions
# It can be accessed by creating an instance of that class

# Object -
# it is an instance of a class
# has some characteristics and behavior
# stores data and the actions it can perform
# when a class is defined no memory is allocated but when it is instantiated
''' Objects take up space in memory and have an associated address like a record in pascal or structure or union. When a program is executed the objects 
 interact by sending messages to one another. Each object contains data and code to manipulate the data. Objects can interact without having to know 
 details of each other’s data or code, it is sufficient to know the type of message accepted and the type of response returned by the objects. '''

# init function also known as dunder init method
''' constructor - used to initialize the object's state
  to initialize data members of a class when object is created
  executed at the time of object creation'''

# self
''' it is a instance of a class that is currently being used
    it has to be the first parameter of any function of a class
    first it is a blank object then new variables are created inside a blank object
    self.name = name -- here first name is not a variable, it is a property of self'''
# object itself is passed as the first argument to the corresponding function

class Point:
    def __init__(self, new_x, new_y):
        self.x = new_x
        self.y = new_y 

    def distance(self):
        return (self.x**2 + self.y**2) ** 0.5
    

p1 = Point(3, 4)
p1.distance() # this can also be written as Point.distance(p1)
Point.distance(p1)
print(p1.__class__)
print(p1.x)

# when we define an variable inside an object then it is called property
# function inside a class is called method

# Built-in functions - len, str, sum, print, range

''' Magic methods
   - dunder init
   - __len__ - used to implement the len() method in python'''

class car:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, i):
        return self.cars[i]
    
    def __repr__(self): # should be used to return a string representing the
                        # object such that with that string you can re create the object fully
                        # printable representation of the object by converting that object to a string.
        return f'<Car {self.cars}>'
    
    def __str__(self): # should be used to return a string that is more suitable for users to read
        return f"Car has {len(self)} cars"
        
ford = car()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(len(ford)) # this without __len__ function will give error (object of type car has no len)
print(ford[1]) # same as print(car.__getitem__(ford, 1))

# to iterate over garage only when you have __getitem__ defined
for i in ford:
    print(i)

print(ford) # here __str__ will be called for repr you have to explicitly mention repr unless and until str is not there

# INHERITANCE - allows us to define a class that inherits all the methods and properties from another class
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)
    
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school) 
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 37.5

rolf2 = Student('Agrima', 'Stanford')
rolf = WorkingStudent('Rolf', 'MIT', 15.5)
rolf.marks.append(12)
rolf.marks.append(13)
rolf.marks.append(14)
rolf.marks.append(15)

print(rolf.weekly_salary())
print(rolf2.average())
print(rolf.average())

''' Decorator @ 
  - changing no argument method into a property
  - used to modify behaviour of a class or function
'''

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    @property
    def calculate(self):
        return sum(self.marks) / len(self.marks)
    
info = Student('Agrima')
info.marks.append(97)
info.marks.append(100)
info.marks.append(93)
print(info.calculate()) # normal way 
print(info.calculate) # to call like this we have to use @property decorator
 
# instance method - caller object as first argument that is self like avg here
class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def avg(self):
        return sum(self.marks) / len(self.marks)

rolf = Student("Agrima")
rolf.marks.append(15)
rolf.marks.append(16)
rolf.marks.append(17)   
print(rolf.avg()) # instance method called as it takes rolf as first argument

# Class method - takes class as first argument
class Foo:
    @classmethod
    def hi(cls): # here cls is a class
        print(cls.__name__)

my_obj = Foo()
my_obj.hi() # here class is passed as first argument 

# Static method - takes no parameters
class Bar:
    @staticmethod
    def hi():
        print("Hello")

obj = Bar()
obj.hi()
Bar.hi() # can be called by class

# adding two objects
class student:
    def __init__(self, name):
        self.name = name
    
    def __add__(self, name1):
        return student(self.name + name1.name)
    
obj1 = student("Hello")
obj2 = student("World")
obj3 = obj1 + obj2
print(obj3.name)

# Adding two list
class student:
    def __init__(self, name):
        self.name = name
    
    def __add__(self, name1):
        demo_obj = student([])
        for i in range(len(self.name)):
            demo_obj.name.append(self.name[i] + name1.name[i])
        return demo_obj
    
obj1 = student([1, 2, 3])
obj2 = student([1, 2, 3])
obj3 = obj1 + obj2

