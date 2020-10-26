import unittest
import pyperclip
from credentials import Credentials

class TestContact(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase:TestCase class that helps in creating test cases
     '''

def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("facebook","Muthoni","muthoni202","virgisonie20@gmail.com") # create contact object

def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account_name,"facebook")
        self.assertEqual(self.new_credentials.user_name,"Muthoni")
        self.assertEqual(self.new_credentials.password,"muthoni202")
        self.assertEqual(self.new_credentials.email,"virgisonie20@gmail.com")

def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials
        objects to our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter","gee","12345678","gee@user.com") 
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2) 

 def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credential from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter","gee","12345678","gee@user.com") 
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)                   

def test_find_credentials_by_email(self):
        '''
        test to check if we can find a credential by email and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter","gee","12345678","gee@user.com") 
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_email("virgisonie20@gmail.com")

        self.assertEqual(found_credentials.user_name,test_credentials.user_name)

def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter","gee","12345678","gee@user.com") 
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("virgisonie20@gmail.com")

        self.assertTrue(credentials_exists)

def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

def test_copy_password(self):
        '''
        Test to confirm that we are copying the password from a found credentials
        '''

        self.new_credentials.save_credentials()
        Credentials.copy_password("virgisonie20@gmail.com")

        self.assertEqual(self.new_credentials.password,pyperclip.paste())                  

if __name__ == '__main__':
    unittest.main()        