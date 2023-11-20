# Python on console

# to run python outside a specific environment

# CONSOLE
'''
- A text interface to your computer
- You can run basically anything by using text. Eg. open files, copy files, run programs
- On windows, open cmd.exe
- On MAC, terminal.app
- On linux, Terminal
'''

# The PATH
'''
- It is a global variable that your operating system uses to specify where to find programs
'''

# Environment variables
'''
PATH is an example of an environment variable
These are just global variables available to all programs that run in the environment
Normally the environment is your compute
'''
# pip - package installer of python

# virtualenv - duplicate an existing Python installation

'''
pip freeze - allows you to save packages that were installed using pip in the virtual environment
pip freeze > requirements.txt - a file will be created having name of all the packages used 
pip install -r requirements.txt - this will install all the packages present in the file. It is beneficial if we share our project with someone else and they run this in there laptop
'''

# pipenv
'''
provide all necessary means to create a virtual environment for your python project
pipfile - tells all the libraries we need
piplock - tells all the versions we need
pipenv run python
a virtual environment created in a separate folder
'''