# DECORATORS
'''
- Higher order functions
- Functions that take other functions as arguments and return a function
- Allows to modify behaviour of a function or method without changing the source code
- Decorators help us to wrap another function in order to extend the behaviour of the 
  wrapped function, without permanently modifying it.
'''
user = {'name': 'Agrima', 'access-level': 'user'}
def user_has_permission(func):
    if user.get('access-level') == 'admin':
        return func
    raise RuntimeError
    

def print_function():
    return f"The name is {user['name']}"

my = user_has_permission(print_function)
print(my())

# 
def user_permission(func):
    def secure_func():
        if user.get('access-level') == 'admin':
            return func()
    return secure_func

def my_func():
    return "Password"

my_secure_function = user_permission(my_func)
print(my_secure_function())


# @syntax
def user_permission(func):
    def secure_func():
        """ secure func docstring"""
        if user.get('access-level') == 'admin':
            return func()
    return secure_func

@ user_permission
def my_func():
    """ docstring """
    return "Password"

print(my_func())
print(my_func.__name__) # secure_func
print(my_func.__doc__)  # secure func docstring 
# to solve this - functools


# Decorators can have arguments passed to them
'''
To add arguments to decorators I add *args and **kwargs to the inner function
- *args will take an unlimited number of arguments of any type such as 10, True etc
- **kwargs will take an unlimited number of keyword arguments, such as count = 99, or name = 'Brandon'
'''

''' Decorators hide the function they are decorating so if i check the __name__ or __doc__
    I will get the inner function as ans
'''
import functools
def user_permission(func):
    @functools.wraps(func)
    def secure_func():
        """ secure func docstring"""
        if user.get('access-level') == 'admin':
            return func()
    return secure_func

@ user_permission
def my_func():
    """ docstring """
    return "Password"

print(my_func())
print(my_func.__name__) # my_func
print(my_func.__doc__) # docstring

# Functools
'''
- Functools module is for higher-order functions that work on other functions
- It provides functions for working with other functions and callable objects to use or
  extend them without completely rewriting them.
'''

# Passing an argument
import functools
def user_permission(func):
    @functools.wraps(func)
    def secure_func(pw):
        """ secure func docstring"""
        if user.get('access-level') == 'admin':
            return func(pw)
    return secure_func

@ user_permission
def my_func(pw):
    """ docstring """
    return f"Password: {pw}"

print(my_func('123'))

# now we cannot create another function using user_permission as decorator without any arguments

# Decorators with parameters
import functools
user = {'name': 'Agrima', 'access-level': 'admin'}

def user_has_permission(access_level):
    def my_decorator(func):
        @functools.wraps(func)
        def secure_func(panel):
            if user.get('access-level') == access_level:
               return func(panel)
        return secure_func
    return my_decorator

# @user_has_permission('admin')
def func(pw):
    return f"Password: {pw}"

one_var = user_has_permission("admin")
two_var = one_var(func("123"))
print(two_var())
#print(func('123'))



# generic decorator using *args and **kwargs
def get_current_user_role():
    return 0

def access_control(access_level: int):
    def new_func(func):
        def decorator(*args, **kwargs):
            if get_current_user_role() <= access_level:
                return func(*args, **kwargs)
            else:
                raise PermissionError("You do not have the proper access level.")
        return decorator
    return new_func

