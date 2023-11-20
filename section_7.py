# DATABASE

# lobal and local scope
''' If there exists two variables with same name in global
and local scope (eg - inside a function), so if you want to access
global variable inside the function you will not be able to access it
because a same variable is in local scope so it will access that instead.
to acces gloabl variable write "global var" inside the function and local varaiable
now does not exist
'''

# _function - pvt - you should not call it but can be called

# Database- a place we can store data, normally organized in tables
''' SQLite 
- software library, small, fast and reliable
- can run in memory or as a single file
- limitation - only one user can write at a time
- multiple reads but limitation on writing
'''

# using SQLite in python
import sqlite3

connection = sqlite3.connect('data.db') # this is a single file containing all my SQLite database
connection.close()
cursor = connection.cursor()

cursor.execute('YOUR SQL QUERY HERE')
connection.commit()

connection.close()
'''
CURSOR
- All operations in SQLite are made by cursors and not by connection
  object itself.
- That is so that we can have one single connection, but multiple cursors
  either reading data and at most one writing data.
- If we tell cursor to read one row it is going to read one row after the one
  it is at now. Eg- it is at one now read then it will read row two and point at row 3
'''

'''
commit()
- Save the result of this query to disk
- Keep a bunch of data in memory until we commit
- we can write multiple things together

'''
# Creating table

connection = sqlite3.connect('data.db')
connection.close()
cursor = connection.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
connection.commit()

# SQLite supports only 5 types of datatypes
#  - NULL
#  - INTEGER - Value is a signed integer, stored in 0, 1, 2, 3, 4, 6, or 8 bytes
#  - REAL - value is a floating point
#  - TEXT - text string, stores using database encoding
#  - BLOB - stored exactly as it was input, binary data field, stores images or documents

# ADD DATA

cursor.execute(f'INSERT INTO books VALUES ("{name}, "{author}", 0)') # This is not considered a good approach beacuse
# if we insert in author - ",0); DROP TABLE books; "
cursor.execute(f'INSERT INTO books VAlues ("{name}","", 0);DROP TABLE books;", 0)') # SQL injection attack

# use this approach to avoid SQL injection
cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author)) # make sure it is a tuple


# SELECT
connection = sqlite3.connect('data.db')
cursor = connection.execute('SELECT * FROM books')
books = cursor.fetchall() # creates a list of tuples [(name, author, read), (name, author, read)]
books = [{"name": row[0], "author": row[1], "read": row[2]} for row in cursor.fetchall()]

# UPDATE
'''UPDATE people SET name = 'JOSE' '''
''' DELETE FROM people WHERE id = 1''' # in SQL '=' for assignment as well as comparison

cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (name,))
connection.commit()
connection.close
cursor.execute('DELETE books WHERE name = ?', (name,))
# Unix timestamp - Number of seconds passed since jan 1, 1970

# SELECT * FROM purchases ORDER BY amount DESC LIMIT 2 # WHERE clause will go before ORDER BY

'''
CONTEXT MANAGER - define an entrance step and an exit step which are run automatically
when the with block is entered and exited
'''
# file 1
import sqlite3
class DatabaseConnection:
    def __init__(self, host):
        self.connection  = None
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
    '''
If an exception is raised; type, value and traceback are passed as arguments to 
__exit__(). Otherwise None arguments are supplied
        # exc_type - exception type - indicates the class of exception
        # exc_val - exception value - indicates the type of exception, like divide by zero, floating_point_errror
        # exc_tb - exception traceback - it is a report which has all of the info needed to solve the exception
'''
# file 2
from name import DatabseConnection
def func():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('')