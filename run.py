#!/usr/bin/env python3.6
import random
from user import User
from credential import Credentians
# user class here


class User:
    '''
    class that generate new instance of users
    '''
    user_list=list() #empty userdetails list

   
    
    def __init__(self, username, password):
        '''
        __init__ method that helps us define properties for our object
        '''
        self.username=username
        self.password=password

    def full_account_details(self):
        '''
        method to display all details of user
        '''
        print(f"Your username is:{self.username}   and your password is:{self.password}")
