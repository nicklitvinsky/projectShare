import UserLogic 

def checkIfUserExisting(username,email,password,login_type):
    #check in database SQL
    if login_type == 1:
        #check if existing in database for sign in
        pass
    elif login_type == 2:
        #check if existing in database for sign in, if not existing, so sign up
        pass



def UserSigningUp():
    login_type = 2
    Registering = UserLogic.UserLogic(None,None,None)
    Registering.Username = input("please enter your username\n")
    Registering.email = input("please enter your email\n")
    Registering.password = input("please enter your password\n")
    #check if the fields are ok
    if UserLogic.UserLogic.UserNameLogic(Registering.Username) and UserLogic.UserLogic.Email_Logic(Registering.email) and UserLogic.UserLogic.Password_Logic(Registering.password):
        #check if the user's fields are matching in SQL
        checkIfUserExisting(Registering.email,Registering.password,login_type)
    else:
        UserSigningUp()#if username or email or password are incorrect    

def UserSigningIn():
    login_type = 1
    username = input("please enter your username\n")
    email = input("please enter your email\n")
    password = input("please enter your password\n")
    #check if the user's fields are matching in SQL
    checkIfUserExisting(username,email,password,login_type)
    


def User_menu():
    print("Welcome user to vacation System, press 1 for sign in or 2 for registering\n")
    try:
        menu = int(input())
        if menu == 1:
            UserSigningIn()
        elif menu == 2:
            UserSigningUp()
        else:
            print("please choose 1 or 2\n")
            User_menu()     
    except:
        print("Invalid selection, please press 1 or 2\n")
        User_menu()



if __name__ == "__main__":
    User_menu()