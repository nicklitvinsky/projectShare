import re
from hashlib import sha3_512
import concurrent.futures



class UserInterFace:
    def __init__(self,Password,email,Username):
        self.password = Password
        self.email = email
        self.Username = Username
        self.Login = False
        self.Userexist = False
       
    ##this function checks the logic of passwords in the sign up and login process
    ## note it also check if the entered password is a common password that is used!
    def Password_Logic(self):
        common_passwords = [
            '123456', 'password', '123456789', 'qwerty', 'abc123', 'Password1',
            '123123', 'welcome', 'admin6', 'letmein'
        ]
           
        try:
            if len(self.password) < 6:
                return "Password must be at least 6 characters long."
            if self.password in common_passwords:
                return "Password is too common. Choose a more secure password."
            if ' ' in self.password:
                return "Password should not contain spaces."
            if not re.search(r'[A-Z]', self.password):
                return "Password must contain at least one uppercase letter."
            if not re.search(r'[a-z]', self.password):
                return "Password must contain at least one lowercase letter."
            if not re.search(r'[0-9]', self.password):
                return "Password must contain at least one digit."
            if not re.search(r'[@$!%*?&]', self.password):
                return "Password must contain at least one special character (e.g., @$!%*?&)."
            if re.search(r'(.)\1', self.password):
                return "Password should not contain repeated characters."
       
            strength = "Strong"
            if len(self.password) < 12:
                strength = "Moderate"
            if len(self.password) < 10:
                strength = "Weak"

            return f"Password is valid. Strength: {strength}"
        except Exception as e:
            print(str(e))

    ##this function checks the logic of entered email in the sign up and login process
    def Email_Logic(self):
        try:
            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

            if not self.email:
                return "Email cannot be empty."
            if not re.match(email_regex, self.email):
                return "Invalid email format. Please provide a valid email address."

            return "Email is valid."
       
        except Exception as e:
            print(f"Error: {str(e)}")
            return "An error occurred while validating the email."
       
    ##this function checks the logic of usernames in the sign up and login process
    def UserNameLogic(self):
        try:
            if not (3 <= len(self.Username) <= 15):
                return "Username - not valid"
            if not self.Username[0].isalpha():
                return "Username - not valid"
            if not re.match(r'^[a-zA-Z0-9_]+$', self.Username):
                return "Username - not vaild"
           
            return "Username - valid"
        except Exception as e:
            print(str(e))


   
    ##note this function will hash  the password that have been entered in the sign up process
    ##note this function will hash every password more then once!
    def hashing_logic_client_side(self, layers=3):
        def hash_password(password):
            current_hash =  password.encode('utf-8')
            for _ in range(layers):
                current_hash = sha3_512(current_hash).digest()
            return sha3_512(current_hash).hexdigest()

        return hash_password(self.password)




if __name__ == "__main__":
    UserInterFace(Password=None,email=None,Username=None)
    #tests
    User = UserInterFace('password123456', 'eladratds@gmail.com','eladR')
    email_r = User.Email_Logic()
    Password = User.Password_Logic()
    Username = User.UserNameLogic()
    print(email_r)
    print(Password)
    print(Username)
