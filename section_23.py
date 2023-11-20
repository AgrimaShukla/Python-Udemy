# Refresher

# numbers that exist before your code runs are integers -5 to 255

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad) # True
print(friends is abroad) # False

lst1 = ["Rolf", "Bob"]
lst2 = ["Rolf", "Bob"]
# print(lst1 is lst2)
print(lst1[0] is lst2[0]) # True

# to recreate an object use repr method

class Book:
    TYPES = ("hardcover", "paperbook")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    @classmethod
    def hardwork(cls, name: str, page_weight: int) -> "Book": # here it is returning book object but as it is of same class we are using " " because uf we will use without " " it will throw an error bcoz this method is created before the class has finished pprocessing
        # if you are using different class object as return type then you can use without " ". eg -> BookShelf
        return cls(name, cls.TYPES[0], page_weight + 100)
        

import sys
print(sys.path) # sys.path where python will look in order to find files to import