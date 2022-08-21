

import sys
usercache = {}
print("Welcome")
while True:
    print("You may create user, delete user, login, change password, or quit")
    wtodo = input("what would you like to do ")
    def add_user():
        username = input("Create your username ")
        password = input("Create your password ")
        if username == username in usercache:
            print("That username is already taken")
        else:
            usercache.update({username: password})
            print(f"Thanks {username} your account has been created")

    def user_quit():
        sys.exit()


    def user_changepword():
        username = input("Enter your username ")
        password = input("Enter your password ")
        usercache.get(username)
        if password == usercache[username]:
            new_pword = input("What would you like your new password to be ")
            usercache.update({username: new_pword})
            print("Your password has been changed")
        else:
            print("incorrect password or username")

    def user_delete():
        username = input("Enter your username ")
        password = input("Enter your password ")
        usercache.get(username)
        if password == usercache[username]:
            usercache.pop(username)
            print("Your account has been deleted")
        else:
            print("incorrect password or username")
    def login():
        username = input("Enter your username ")
        password = input("Enter your password ")
        usercache.get(username)
        if password == usercache[username]:
            print("You have logged in")
        
        

    if wtodo == "create user":
        add_user()
    elif wtodo == "delete user":
        user_delete()
    elif wtodo == "quit":
        user_quit()
    elif wtodo == "change password":
        user_changepword()
    elif wtodo == "login":
        login()
    else:
        print("that is not an option")
    
