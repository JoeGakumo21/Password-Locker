
import unittest # Importing the unittest module
from user import User # Importing the user class


class  TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    #first test
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Joseph Gakumo","Joegakumo123456") # create contact object   ,"Facebook","JosephGakumo","joegakumo1@gmail.com"


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Joseph Gakumo")
        self.assertEqual(self.new_user.password,"Joegakumo123456")
    if __name__ == '__main__':
         unittest.main()   