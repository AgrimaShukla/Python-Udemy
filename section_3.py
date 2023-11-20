# Milestone project

movies = []

def add():
   title = input("Enter title of the movie: ")
   director = input("Enter the movie director: ")
   year = input("Enter the movie release year: ")
   movies.append({
   "title": title,
   "director": director,
   'year': year
})

def print_output(movie):
        print(f"Title: {movie['title']}, Director: {movie['director']}, Year: {movie['year']}")

def show():
   for movie in movies:
      print_output(movie)

def find():
   name = input("Enter movie name: ")
   for movie in movies:
      if movie["title"] == name:
         print_output(movie)
         break
   else:
      print("Invalid")

'''user_input = {
   "1": add,
   "2": show,
   "3": find
}

user_choice = input("Enter any one of the options:\n1) Add\n2) Show all the movies (Show) \n3) Find a movies (Find)\n4) Quit (q)\nEnter: ")
   
while user_choice != "q":
    if user_choice in user_input:
        option = user_input[user_choice] 
        option()
    else:
       print("Invalid option")

    user_choice = input("Enter any one of the options:\n1) Add\n2) Show all the movies (Show) \n3) Find a movies (Find)\n4) Quit (q)\nEnter: ")

'''
while True:
   user_input = input("Enter any one of the options:\n1) Add\n2) Show all the movies (Show) \n3) Find a movies (Find)\n4) Quit (q)\nEnter: ")

   if user_input == "1":
      add()
   elif user_input == "2":
      show()
   elif user_input == "3":
      find()
   elif user_input == "q":
      break
   else:
      print("Invalid")