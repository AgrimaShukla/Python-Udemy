from user import User
from database import Database

class Admin(User): # Admin is an instance of Saveable
    def __init__(self, username, password, access):
        super().__init__(username, password)
        self.access = access

    def __repr__(self):
        return f"Admin {self.username}, access {self.access}>"
    
    def to_dict(self):
        return{
            'username': self.username,
            'password': self.password,
            'access': self.access
        }
    
   