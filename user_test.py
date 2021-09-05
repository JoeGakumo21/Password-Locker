
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
        # self.assertEqual(self.new_user.accountname,"Facebook")
        # self.assertEqual(self.new_user.fullname," Joseph Gakumo")
        # self.assertEqual(self.new_user.email,"joegakumo1@gmail.com")

    #creation of tearDown here
    def tearDown(self):
         '''
        tearDown method that does clean up after each test case has run. 
         '''
         User.user_list=[]
    

    #second test
    def test_save_user(self):
        '''
        test_save_user_details test case to test if the user object is saved into
         the object list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)

    #third test 
    def test_save_multiple_users(self):
        '''
        method to save multiple account in the same user locker password
        '''     
        self.new_user.save_user()
        test_user=User("Joseph Gakumo", "Joegakumo1234455")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

if __name__ == '__main__':
    unittest.main()