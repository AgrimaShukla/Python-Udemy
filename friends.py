# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to nearby_friends.txt
friend = input("Enter names separated by commas: ").split(',')
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
    friends_nearby_file.write(f'{friend}\n')

friends_nearby_file.close()