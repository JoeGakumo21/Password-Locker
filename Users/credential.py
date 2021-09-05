from .user import User
import random
import string

class Credentials:
    '''
    This class handles credentials of our user
    '''
    Credentials=[]

    def __init__(self,account,username,password):
        '''
        method that initialise our object user
        '''
        self.account=account
        self.username=username
        self.password=password

    def __str__(self):
        '''
        methods that output the user details inform of a string
        '''
        return "Your Username: " + self.username +" \n Your password is:"+ {self.password}

    def __repr__(self):
        '''
        m,ethod that return all credentials
        '''
        return (f'Credentials {self.account} {self.username} {self.password}')

                