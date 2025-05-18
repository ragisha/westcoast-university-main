#Login Authentication
class Validation():

    def __init__(self,uname,pwd):
        self.uname=uname
        self.pwd=pwd
#checks if the username and password are of same value to login
    def toValidate(self):
        if self.uname == self.pwd: 
            print("\nAuthentication successful!!")
            return True
        else:
            print("\nAuthentication Failed!!")
            return False