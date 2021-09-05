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
# added the credential class

credentians_list=[]
class Credentians:
    '''
    this class generate new instances of credentials to class user
    '''
    def __init__(self, account,fullname,phonenumber,email ):
        '''
        method that help populate the user  created
        '''
        self.account=account
        self.fullname=fullname
        self.phonenumber=phonenumber
        self.email=email

    def user_details(self):
        '''
        method to create credentials of the user
        '''
        Credentians.credential_list.append()
        print(f"{self.account}{self.fullname}{self.phonenumber}{self.email}")

