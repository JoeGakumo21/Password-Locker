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

if __name__ == "__main__":
        password_locker_main()

































# import random
# from user import User
# from credential import Credentians
# # user class here
# def main():
#     '''
#     Main function to execute all functions created

#     '''
#     #=================================
# class User:
#     '''
#     class that generate new instance of users
#     '''
#     user_list=list() #empty userdetails list

   
    
#     def __init__(self, username, password):
#         '''
#         __init__ method that helps us define properties for our object
#         '''
#         self.username=username
#         self.password=password

#     def full_account_details(self):
#         '''
#         method to display all details of user
#         '''
#         print(f"Your username is:{self.username}   and your password is:{self.password}")

# #credential class here

# credentians_list=[]
# class Credentians:
#     '''
#     this class generate new instances of credentials to class user
#     '''
#     def __init__(self, account,fullname,phonenumber,email ):
#         '''
#         method that help populate the user  created
#         '''
#         self.account=account
#         self.fullname=fullname
#         self.phonenumber=phonenumber
#         self.email=email

#     def user_details(self):
#         '''
#         method to create credentials of the user
#         '''
#         Credentians.credential_list.append()
#         print(f"{self.account}{self.fullname}{self.phonenumber}{self.email}")


#         #main function here

#     print("Hellow there, Welcome to Password locker \n")

# #displaying the output of our user ================================
#     # username=input("Enter Username: ")
#     # password= input("Enter a strong password: ")
#     # our_user=User(username, password)
#     # our_user.full_account_details()

#     # #function to print our username and password in a string
#     # def __str__(self,username,password):
#     #     '''
#     #     method to print our details in a one line
#     #     '''
#     #     print(f"{username} {password}")
        
# #==========================================================another section here
#     users_input = " "
#     while users_input != "q":
#         print("Available options")
#         print("1 - Enter to create a new account")
#         print("2 - Display all the account")
#         print("3 -login to your account")
#         print ("q - quit the program")

#         users_input = input("Select Option to continue: ")

#         #=================Functions if to allow user iteract with the application================================

#         if users_input== "1":

#             print("Enter type of Account to create eg ..Instagram, Facebook, Whatsapp, Tweeter")
#             account=input()

#             print("Create Username")
#             username=input()

#             print("create password")
#             created_user_password=input()

#             print("Confirm password")
#             confirm_password=input()

#             print("Enter your phone number")
#             user_phonenumber=input()

#             print("Enter your email address")
#             user_email_address=input()
#             # print(f"Created {account} account\n Your full name is: {username}\n Your password is: {created_user_password}\n Your phone number is :{user_phonenumber}\n Your personal email address is: {user_email_address}")
            
#             #========================================
#             while confirm_password!=created_user_password:
#                 print("Invalid password , the password didn't match!")
#                 print("Enter your Password once more")
#                 created_user_password=input()
#                 print("Confirm the entered password")
#                 confirm_password=input()

#             else:
#                 print(f"{account} Account created successfully, Congratulation {username}\n ")    
#                 print("proceed to Login \n Enter UserName")
#                 entered_username=input()
#                 print("Enter your password:")
#                 entered_password=input()


#             while entered_username != username or entered_password !=created_user_password:
#                 print("The username or password entered dont match, Kindly check and try again")
#                 print("Enter the Username")
#                 entered_username=input()
#                 print("enter the Password")
#                 entered_password=input()

#             else:
#                 print(f"Welcome: {username} to your account\n")    
#                 print("Below is a summary of your account")
#                 print(f"Created {account} account\n Your full name is: {username}\n Your password is: {created_user_password}\n Your phone number is :{user_phonenumber}\n Your personal email address is: {user_email_address}")
                
#         elif users_input =="2":
#                 print("Kindly Login  \n Enter UserName")
#                 entered_username=input()
#                 print("Enter your password:")
#                 entered_password=input()
#                 print(f"Created {account} account\n Your full name is: {username}\n Your password is: {created_user_password}\n Your phone number is :{user_phonenumber}\n Your personal email address is: {user_email_address}")

                    
        
        
#         elif users_input == "3":
#             print("Welcome Back!!")
#             print("Enter username\n")
#             default_user_name=input()

#             print("Enter password\n")
#             default_user_password=input()
#             print("\n")


#             while default_user_name !="JosephGakumo" or default_user_password !="Joegakumo123.":
#                 print("Wrong details provided for username and password, kindly try again or use the default username:JosephGakumo and password:Joegakumo123.")
#                 print("Enter username")
#                 default_user_name=input()
#                 print("Enter password")
#                 default_user_password=input()
#                 print("\n")  
#             else:
#                 print(f"{default_user_name} Login successfuly \n\n\n")
#                 print(f"Created {account} account\n Your full name is: {username}\n Your password is: {created_user_password}\n Your phone number is :{user_phonenumber}\n Your personal email address is: {user_email_address}")
                

#         elif users_input.lower() == "q":            
#             break
            
            
#     else:
#             print("Thank you for accessing our services, your password are safe with password lockers ")    
#             print({default_user_name})  
#             # 

#     if __name__ == '__main__':

#         main()