# FILES

''' Reading a file '''
my_file = open('file.txt', 'r') 
# .read gives us all the file content as a single string
file_content = my_file.read()
# there is a certain limit on no of files opened at a time
my_file.close()
print(file_content)

''' Writing in a file '''
user_name = input("Enter your name: ")
my_writing = open('file.txt', 'w') # 'w' will overwrite everything in the file
my_writing.write(user_name)
my_writing.close()

''' Copying a file '''

# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to nearby_friends.txt
friend = input("Enter names separated by commas: ").split(',') # splits a string into a list
people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]
''' without strip- {'Agrima\n', 'Meghna\n', 'Shruti\n', 'Meher\n', 'Niyati\n'} 
    with strip- {'Agrima', ... }'''
# strip() method removes any trailing and leading white spaces
people.close()
''' readlines() method returns a list containing each line in the file as a list item
'''
friends_set = set(friend)
people_nearby_set = set(people_nearby)
friends_nearby_set = friends_set.intersection(people_nearby_set)

friends_nearby_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f"{friend} is nearby")
    friends_nearby_file.write(f'{friend}')

friends_nearby_file.close()


''' CSV files in python '''

files = open('file.txt', 'r')
lines = files.readlines()
# to ignore first line in file
lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data = line.split(',')
    name = person_data[0]
    age = person_data[1]
    place = person_data[2]

    print(f'{name.title()} is {age} years old living in {place.capitalize()}')

# to separate values using comma
sample_csv = ','.join(['Meghna', '20', 'Noida up'])

'''JSON - Javascript object notation'''
# JSON is a text format for storing and transporting data
# json is a string
# should always use " " not ' '
# dictionary in python is an object in js

import json
# json module is not an object or a class

file = open('file_json.txt', 'r')
file_contents = json.load(file) # reads file and turns it into a dictionary
# json.load() takes file object as a parameter and returns json object which is dictionary in python
file.close()
print(file_contents['friends'][0])

# to covert dictionary to json object - dump
new_dict = [
    {"name": "Agrima", "Age": 21},
    {"name": "Niyati", "Age": 22}
]

dict_to_json = open('nearby_friends.txt', 'w')
json.dump(new_dict, dict_to_json)
dict_to_json.close()

# json loads() - takes JSON string and converts to dictionary
my_json_string = '[{"name": "Mahak", "place": "Assam"}]'
new_file = json.loads(my_json_string)
print(new_file[0]['name'])

# IMP - Json allows us to use list and dictionaries not tuples

'''Opening and closing file automatically'''
# with - closing resources right after opening and processing  them
with open('file_json.txt', 'r') as file:
     file_contents = json.load(file)

'''Importing our own files'''
def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read() # 'Rolf\nCharlie\n' so use .split('\n') {Rolf, charlie}
    
# in a new file
import random1 # or from random1 import save_To_file (function name)
random1.save_to_file('WHyyyy', 'nearby_friends.txt')

# at background the python is maintaining a dictionary with name of function to function contents

def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i
        
    raise NotFoundError(f'{expected} not found in provided iterable')

class NotFoundError(Exception):
    pass

# relative import is an import that starts from current file
# circular import -  does not work
if __name__ == '__main__': # this means when you run file as a script not as a module
   print("name")