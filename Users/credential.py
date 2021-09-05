from .user import User
import random
import string
from .userDetails import read_from_file, write_to_file

data_file = "credentials.csv"
class Credentials:
    '''
    This class handles credentials of our user
    '''
    credentials=[]

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

    @classmethod
    def verifyDetails(cls, username,password):
        '''
        method to verifty if a user exist
        '''            

        our_user_details=  ''
        for user in User.users:
            if user.username==username and user.password==password:
                our_user_details=user.username
                return our_user_details

    def save_credentials(self):
        write_to_file(data_file,self)
        Credentials.credentials.append(self)

    print(credentials)     

    @classmethod
    def search_credentials(cls,account):
        '''
        method that search an existing account
        '''     
        for credentials in cls.credentials:
            if credentials.account==account:
                return credentials.__repr__()
    @classmethod
    def display_credentials(cls):
        '''
        method that displays the account details
        '''
        read_from_file("users.csv")
        read_from_file("credentials.csv")
        return cls.credentials            
    @classmethod
    def delete_credentials(cls,account):
        '''
        method that checks if a user exist and delete it 
        '''
        for  credentials in cls.credentials:
            if credentials.account == account:
                cls,credentials.remove(credentials)
                return cls.credentials

    @classmethod
    def check_if_credentials_exist(cls,account):
        '''
        method that checks existence of a credentials
        '''
        for credentials in cls.credentials:
            if credentials.account==account:
                return True
        return False

    def generate_credentials_password(length=10):
        '''
        method to autogenerate password to a user
        '''
        password= string.ascii_lowercase+string.digits + string.ascii_uppercase + "=+_)(*&^%$#@!~?><"
        return "".join(random.choice(password) for _ in range(length))