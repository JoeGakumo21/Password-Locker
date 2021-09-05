#import userDetails.py
from .userDetails import read_from_file, write_to_file

data_file = "users.csv"

class User:
    '''
    A user class initialization
    '''

    users= []
    def __init__(self,username, password) :
        """
        Args:
        Username(string)
        password(string)
        """
        self.username=username
        self.password=password

    #method to save user details
    def save_user(self):
        '''        
        saving Users
        '''     
        write_to_file(data_file, self)
        User.users.append(self)

        #method to display username in string
    def __repr__(self) -> str:
        return f"{self.username}"  


    @classmethod
    def show_user(cls):
        return cls.users      

    def find_by_username(cls,username):
        '''
        method to find the user using username
        '''    
        for user in cls.users:
            if user.username==username:
                return user
    def find_user(cls):
        '''
        method to find user in the list
        '''            
        return cls.users

    def delete_user(cls,username):
        '''
        method to delete an existing user
        '''
        for user in cls.users:
            if username==username:
                cls.users.remove(user)
                return True
            return False    

    def del_user(self):
        '''
        method to delete a single user
        '''
        User.users.remove(self)
        return True