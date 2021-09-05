#!/usr/bin/env python3.6
import random
from user import User
from credential import Credentians
# user class here
def main():
    '''
    Main function to execute all functions created

    '''
    #=================================
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

#credential class here

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


        #main function here

    print("Hellow there, Welcome to Password locker \n")

#displaying the output of our user ================================
    # username=input("Enter Username: ")
    # password= input("Enter a strong password: ")
    # our_user=User(username, password)
    # our_user.full_account_details()

    # #function to print our username and password in a string
    # def __str__(self,username,password):
    #     '''
    #     method to print our details in a one line
    #     '''
    #     print(f"{username} {password}")
        
#==========================================================another section here
    users_input = " "
    while users_input != "q":
        print("Available options")
        print("1 - Enter to create a new account")
        print("2 - Display all the account")
        print("3 -login to your account")
        print ("q - quit the program")

        users_input = input("Select Option to continue: ")

        #=================Functions if to allow user iteract with the application================================

        if users_input== "1":

            print("Enter type of Account to create eg ..Instagram, Facebook, Whatsapp, Tweeter")
            account=input()

            print("Create Username")
            username=input()

            print("create password")
            created_user_password=input()

            print("Confirm password")
            confirm_password=input()

            print("Enter your phone number")
            user_phonenumber=input()

            print("Enter your email address")
            user_email_address=input()
            # print(f"Created {account} account\n Your full name is: {username}\n Your password is: {created_user_password}\n Your phone number is :{user_phonenumber}\n Your personal email address is: {user_email_address}")
            
            #========================================
            while confirm_password!=created_user_password:
                print("Invalid password , the password didn't match!")
                print("Enter your Password once more")
                created_user_password=input()
                print("Confirm the entered password")
                confirm_password=input()

            else:
                print(f"{account} Account created successfully, Congratulation {username}\n ")    
                print("proceed to Login \n Enter UserName")
                entered_username=input()
                print("Enter your password:")
                entered_password=input()


            while entered_username != username or entered_password !=created_user_password:
                print("The username or password entered dont match, Kindly check and try again")
                print("Enter the Username")
                entered_username=input()
                print("enter the Password")
                entered_password=input()

            else:
                print(f"Welcome: {username} to your account\n")    
                print("Below is a summary of your account")
                print(f"Created {account} account\n Your full name is: {username}\n Your password is: {created_user_password}\n Your phone number is :{user_phonenumber}\n Your personal email address is: {user_email_address}")
                
        elif users_input =="2":
                print("Kindly Login  \n Enter UserName")
                entered_username=input()
                print("Enter your password:")
                entered_password=input()
                print(f"Created {account} account\n Your full name is: {username}\n Your password is: {created_user_password}\n Your phone number is :{user_phonenumber}\n Your personal email address is: {user_email_address}")

                    
        
        
        elif users_input == "3":
            print("Welcome Back!!")
            print("Enter username\n")
            default_user_name=input()

            print("Enter password\n")
            default_user_password=input()
            print("\n")


            while default_user_name !="JosephGakumo" or default_user_password !="Joegakumo123.":
                print("Wrong details provided for username and password, kindly try again or use the default username:JosephGakumo and password:Joegakumo123.")
                print("Enter username")
                default_user_name=input()
                print("Enter password")
                default_user_password=input()
                print("\n")  
            else:
                print(f"{default_user_name} Login successfuly \n\n\n")
                print(f"Created {account} account\n Your full name is: {username}\n Your password is: {created_user_password}\n Your phone number is :{user_phonenumber}\n Your personal email address is: {user_email_address}")
                

        elif users_input.lower() == "q":            
            break
            
            
    else:
            print("Thank you for accessing our services, your password are safe with password lockers ")    
            print({default_user_name})  
            # 

    if __name__ == '__main__':

        main()