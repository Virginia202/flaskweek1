#!/usr/bin/env python3.6
from credentials import Credentials

def create_credentials(aname,uname,passw,email):
    '''
    Function to create a new credential
    '''
    new_credentials = Credentials(aname,uname,passw,email)
    return new_credentials

def save_credentials(w,x,y,z):
    '''
    Function to save credentials
    '''
    cred = Credentials(w,x,y,z)
    Credentials.save_credentials(cred)

def del_credentials(credential):
    '''
    Function to delete a credential
    '''
    credentials.delete_credentials()  

def find_credentials(email):
    '''
    Function that finds a credential by email and returns the credentials
    '''
    return Credentials.find_by_email(email)

def check_existing_credentials(email):
    '''
    Function that check if a credentials exists with that email and return a Boolean
    '''
    return Credentials.credentials_exist(email)  

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def welcome():
    print("Hello Welcome to password locker.What is your name")
    user_name = input()

    print(f"Hello{user_name}.what would you like to do?")
    print('\n')
    main()
def main():
   

 
    print("Use these short codes : cc - create a new account, dc - display credentials, fc -find credentials, ex -exit  ")

    short_code = input().lower()

    if short_code == 'cc':
        print("New Account")
        print("-"*10)

        print ("Account name ....")
        a_name = input()

        print("User name ...")
        u_name = input()

        print("Password...")
        passw = input()

        print("Email address ...")
        e_address = input()


        save_credentials(a_name,u_name,passw,e_address) 
        print ('\n')
        print(f"New Contact {a_name} {u_name} created")
        print ('\n')
        main()
    elif short_code == 'dc':

        if display_credentials():
                print("Here is a list of all your credentials")
                print('\n')

                for credentials in display_credentials():
                        print(f"{credentials.account_name} {credentials.user_name} .....{credentials.password}")

                print('\n')
        else:
                print('\n')
                print("You dont seem to have any credentials saved yet")
                print('\n')
        main()
    elif short_code == 'fc':

        print("Enter the email you want to search for")

        search_email = input()
        if check_existing_credentials(search_email):
                search_credentials = find_credentials(search_credentials)
                print(f"{search_credentials.account_name} {search_credentials.user_name}")
                print('-' * 20)

                print(f"Email address.......{search_credentials.email}")
                print(f"User name.......{search_credentials.user_name}")
        else:
                print("That account does not exist")

    elif short_code == "ex":
        print("Bye .......")
        # break
    else:
        print("I really didn't get that. Please use the short codes")
        main()
welcome()
