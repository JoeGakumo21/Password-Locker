
import unittest # Importing the unittest module
from Users.credential import Credentials
from Users.user import User
class  UserTest(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    #first test
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.user = User("Joseph Gakumo","Joegakumo123456") # create contact object   ,"Facebook","JosephGakumo","joegakumo1@gmail.com"
    # first test
    def  test_create_user(self):
        '''
        method to test a new user created
        '''
        self.assertEqual(self.user.username, "Joseph Gakumo")
        self.assertEqual(self.user.password, "Joegakumo123456")

    #second test
    def test_save_user(self):
        '''
        test to test when a user has been saved
        '''
        User.users =[]
        self.user.save_user()
        self.assertEqual(len(User.users),1)

    #third test
    def test_save_multiple_users(self):
        '''
        test to be tested when multiple users are saved
        '''    
        User.users = []
        self.user.save_user()
        test_user = User('test', 'test')
        test_user.save_user()
        self.assertEqual(len(User.users), 2)
    def test_delete_user(self):
        '''
        test to delete a user
        '''
        # User.users = []
        self.user.save_user()
        test_user = User('test', 'test')
        test_user.save_user()
        self.user.delete_user(test_user.username)
        self.assertEqual(len(User.users), 1)
    
    def tearDown(self):
        User.users = []


# credentials test
#first test

class CredentialTest(unittest.TestCase):
    def setUp(self):
        '''
          Set up method to run before each test cases.
        '''
       

if __name__ == '__main__':
    unittest.main()