from Student import Students
from Professor import Professors
from Registrar import Registrar
from Validation import Validation
class Main:

    #1. To call Students Class
    def doStudent(self):
        stud=Students.exec()

    #2. To call Professors Class
    def doProfessor(self):
        prof=Professors.exec()

    #3. To call Registrar Class
    def doRegistrar(self):
        reg=Registrar.exec()
    
    #4. Constructor and Welcome page
    def __init__(self):
        print("""
        * * * * * * * WESTCOAST UNIVERSITY * * * * * * *

        * * * * * STUDENTS REGISTRATION SYSTEM * * * * *

        * * * * * * * * * L O G I N  * * * * * * * * * * \n""")
        uname=input("Enter the Username : ")
        pwd=input("Enter the Password : ")
        valid=Validation(uname,pwd)
        if(valid.toValidate()):
            print("""
        * * * * * * * D E S I G N A T I O N  * * * * * *""")
            print("\n1.Student\n2.Professor\n3.Registrar\n")
            while(True):
                ch = int(input("Enter choice:\n"))
                if ch==1:
                    self.doStudent()
                    break
                elif ch==2:
                    self.doProfessor()
                    break
                elif ch==3:
                    self.doRegistrar()
                    break
                else:
                    print("Invalid Choice!!\n")
obj=Main()
