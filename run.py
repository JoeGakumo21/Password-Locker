#!/usr/bin/env python3.6
from hashlib import new
from  Users.user import User
from Users.credential import Credentials


def create_our_user(username,password):
    '''
    method to create a new users account
    '''
    new_user= User(username, password)
    return new_user
def save_our_user(user):
    '''
    method to save the user created
    '''    
    user.save_user()

def show_user(user):
    '''
    method to show or display a user that have initially created
    '''
    user.show_user_created()    

def login(username,password):
    '''
    method that allow an already existing user to login to the account
    '''    
    verified_user_details=Credentials.verifyDetails(username, password)
    return verified_user_details

def create_credentials(account, username, password):
    '''
    function that create a new credential
    '''
    new_credential= Credentials(account, password, username)
    return new_credential

def save_credentials(credentials):
    '''
    method to save a new created  credentials of the account 
    '''
    Credentials.save_credentials(credentials)

def delete_credentials(credentials):
    '''
    method to delete a credentials
    '''
    Credentials.delete_credentials(credentials)

def search_credentials(account):
    '''
    method that allow search an existing credential
    '''
    return Credentials.search_credentials(account)

def show_all_credentials():
    '''
    method to display all the credentials of a user
    '''
    return Credentials.display_credentials()

def generate_credentials():
    '''
    method to generate password
    '''    
    auto_generate_password_user= Credentials.generate_credentials_password()
    return auto_generate_password_user



def password_locker_main():
    '''
    This is the main function that will be called to execute the program
    '''
    welcome_message="Hello, welcome to Password Locker Account creation \n Follow the following steps to create accout or Login in \n 1. You new here, Create a new Account \n 2. Have one already Created , Kindly login \n"
    user_input= input(welcome_message).lower().strip()
    
    # print(user_input)

    if user_input == "1":
        print("Great! Welcome to password Locker account creation")
        username=input("Enter your password: ")
        while True:
            '''
            method that allow user to choose whether to create password or it be generated
            '''
            password_message= """
            1. create a pasword for the account\n
            2. use a generated password\n
            """
            password_message= input(password_message).lower().strip()
            if password_message == "1":
                password = input("Enter your password: ")
            elif password_message == "2":
                password =generate_credentials()
                print("Press 2 to access other services")
                break 
            else:
                print("Invalid Password")
        save_our_user(create_our_user(username, password)) 
        print(f"Hellow {username} Your account has been created successfully and your password is {password}")      
            
    elif user_input == "2":
        print ("Great! Welcome back, lets Login\n")
        username = input("Enter your username: ")
        password =input("Enter your password: ")
        details_verification= login(username, password)
        if details_verification == login(username, password):
            print (f"Welcome back {username} Your accounts details matched and account verified")
        else:
            print("Invalid uisername or Password, Kindly try another means")    

    while True:
        logged_in_details = """
        1. Create credentials for new person \n
        2. Search credentials  for the existing user \n
        3. Display credential  for the users \n
        4. Delete credentials for the user \n
        """
        logged_in_details= input(logged_in_details).lower().strip()
        if logged_in_details == "1":
            print ("Great  lets create a new credentials")
            account= input("Enter account  to print: ")
            username= input("Enter your username: ")
            my_pass_message = """
            1. Create a password for the account\n
            2. Use a generated password\n
            """
            response=input(my_pass_message).lower().strip()
            if response == "1":
                password = input("Enter your password: ")
                print(f"Your credentials for  {account} created successfully")
            elif response== "2":
                password=generate_credentials()
                save_credentials(create_credentials(account, username, password))
                print(f" Credentials for  {account}  created successfuly")
        elif logged_in_details =="2":
            '''
            method to search credential for an existing user
             '''
            print("Great! Let's search credentials")
            account = input("Enter your account name: ")
            search_credentials(account) 
        elif logged_in_details == "3":
            '''
            function to show details of the credential
            '''   
            if show_all_credentials():
                print("Great! Let's display credentials\n")
                print("Here's a list of all your credentials\n")
                for credentials in show_all_credentials():
                    print(f'Account: {credentials.account}\nUsername: {credentials.username}\nPassword: {credentials.password} \n')
            else:
                print("You don't have any credentials saved yet")
        elif logged_in_details == "4":
            '''
            function to delete an existing credential
            '''
            print("Great! Let's delete credentials")
            account = input("Enter your account name: ")
            delete_credentials(account)
if __name__ == "__main__":
        password_locker_main()



