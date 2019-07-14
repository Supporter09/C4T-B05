import sys 
 
def login(username, password):
    # Assuming you just want to test this and keep the data in the source file
    accounts = {'donaldtrump': 'p07u5Man',
                'admin': 'admin'}
    if password == accounts[username]:
        return True
    return False
 
def main():
    login_tries = 0
    if login_tries > 5:
        sys.exit()
        # To prevent infinite login attempts 
    user, pw = input("Username: "), input("Password: ")
    if login(user, pw):
        print("Login successful!")
        # Do stuff
    else:
        print("Wrong username or password!")
        login_tries += 1

