class MyClass:
    __var = 10
    def __init__(self):
        self.__private_variable = 10

    def __private_method(self):
        return "This is a private method."

# Creating an instance of MyClass
obj = MyClass()

# Accessing private variable and method using name mangling
print(obj._MyClass__private_variable)  # Output: 10
print(obj._MyClass__private_method())
print(MyClass._MyClass__var)  # Output: This is a private method.
