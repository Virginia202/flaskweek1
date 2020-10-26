class Credentials:
    '''
    class that generates new instances of credentials
    '''

    credentials_list = []

    def __init__(self,account_name,user_name,password,email):

        self.account_name = account_name
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_credentials(self):

        '''
        save_credentials method saves contact objects into contact_list
        '''

        Credentials.credentials_list.append(self)

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credential from the credentials_list
        '''

        Credentials.credentials_list.remove(self) 


    @classmethod
    def find_by_email(cls,email):
        '''
        Method that takes in an email and returns credentials that matches that email.

        Args:
            email: email address to search for
        Returns :
            Credentials of person that matches the email.
        '''

        for credentials in cls.credentials_list:
            if credentials.email_address == email:
                return credentials   

    @classmethod
    def credentials_exist(cls,email):
        '''
        Method that checks if credentials exists from the credentials list.
        Args:
            email: email address to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.email == email:
                    return True

        return False                      

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list  

    @classmethod
    def copy_passwor(cls,email):
        credentials_found = Credentials.find_by_email(email)
        pyperclip.copy(credentials_found.email)        