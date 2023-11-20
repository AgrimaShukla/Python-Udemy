# For division we get float value
print(12/3)
# To remove decimal
print(12//3)

# format - used for formatting strings by embedding values in the placeholders
name = "Agrima"
final_greeting = "How are you {}?"
greeting = final_greeting.format(name)
print(greeting)

age = input("Enter age: ") # input 3
print(f"You have lived {age*12} months") # here the output will be 333333333333 (12 times 3) beacuse input takes input a string 

default_value = "there"
val = input("Enter your name: ")
name =  val or default_value
print(f"Hello, {name}!")

x=True
cmp=x and 18 #output- 18, if the value on left is true then we get the value on right of and 

# LISTS
# append vs extend
friends = ["Agrima", 1, 1.5, True]
friends.append("Shukla")
friends.remove(1)
print(friends)

friend=["Agrima", "Niyati", "Meher"]
friend = ", ".join(friend)
print(friend)

# TUPLE
friends = ("Agrima", 1, True)
#friends.append(2) # Error
friends = friends + (2,)
print(friends)

# SET 
friends = {"Agrima", "Niyati"}
friends.add("Meher")
#friends.append("xyz") # Error

# DICIONARY
friends_age = {"Agrima": 21, "Niyati": 20}
friends_age["Mahak"]=21 # add value

# Dictionary using tuples
friends = (
    {"name": "agrima", "age": 21},
    {"name": "Niyati", "age": 20}
)
print(friends)

