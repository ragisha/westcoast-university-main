from DefaultClass import *
from DefaultStudent import *
from DefaultProfessor import *
from AdminClass import *

class Registrar(DefaultCourse,DefaultStud,DefaultProf):

    #1.Constructor
    def __init__(self):
        super().__init__()

    #2. To Display All Students
    def viewStudent():
        std=studDetails.getDetails()
        print("""\n
        * * * * * S T U D E N T  D E T A I L S * * * * * \n""")
        for i in range(1,len(std)):
            Registrar.displayStudent(std[i])

    #3. To Display All Professors
    def viewProfessor():
        professor=profDetails.getDetails()
        print("""\n
        * * * * * P R O F E S S O R  D E T A I L S * * * * * \n""")
        for i in range(1,len(professor)):
            Registrar.displayProfessor(professor[i])

    #4. To Register New Student
    def registerStudent():
        studentDetails={}
        print("""\n
        * * * * * S T U D E N T  R E G I S T R A T I O N * * * * * \n""")
        name=input("\nEnter Student name : \n")
        dob=input("\nEnter Student's Date of Birth : \n")
        address=input("\nEnter student's address : \n")
        course=[]
        course=input("\nEnter the course selected by students : \n")
        studentDetails["Name"]=name
        studentDetails["DateOfBirth"]=dob
        studentDetails["Address"]=address
        studentDetails["course"]=course
        print(studentDetails)

    #5. To Register New Professor
    def registerProfessor():
        professorDetails={}
        print("""\n
        * * * * * P R O F E S S O R  R E G I S T R A T I O N * * * * * \n""")
        name=input("\nEnter Professor name : \n")
        course=input("\nEnter the Course they opted to teach : \n")
        professorDetails["Name"]=name
        professorDetails["course"]=course
        print(professorDetails)
    
    #6. To Add New Course
    def addCourse():
        print("""
        * * * * * A D D   C O U R S E * * * * *\n""")
        while(True):
            sem=int(input("Enter course semester : "))
            if(sem>0 and sem<9):
                break
            else:
                sem=int(input("Enter course semester : "))
        courseList=DefaultCourse()
        sub=courseList.chooseCourse(sem)
        print(sub)
        while(True):
            print("\n1.Add course \n2.Back")
            c = int(input("\nEnter choice:\n"))
            if c==1:
                newCourse=[]
                newCourse = input("\nEnter course to append : \n")
                if newCourse in sub:
                    print("Course Exist!!")
                else:
                    sub.append(newCourse)
                    print("\nNew course List of the sem : ")
                    print(sub)
            elif c==2:
                break
    
    #7. To check for number of Students registered for the course
    def toCheck(search_word):
        nested_list=profDetails.delDetails()
        results = [sub_list[2] for sub_list in nested_list if sub_list[1] == search_word]
        if results == []:
            return 0
        else:
            return len(results[0])   

    #8. To freeze course if count is greater than 10
    def freezeCourse():
        print("""
        * * * * * F R E E Z E   C O U R S E * * * * *\n""")
        course=input("Enter course to freeze : ")
        check=Registrar.toCheck(course)
        if(check==10):
            print("\nMax count reached!! Course "+course+" is freezed")
            print("\nNotify students: "+course+" is Freezed")
        else:
            print("\nMax count not reached !!\nTotal number of students enrolled to the Course "+course+" is ",check)

    #9. To delete course if less than 3 students have choosen it
    def deleteCourse():
        print("""
        * * * * * D E L E T E   C O U R S E * * * * *\n""")
        while(True):
            sem=int(input("Enter course semester : "))
            if(sem>0 and sem<9):
                break
            else:
                print("Invalid Input")
        courseList=DefaultCourse()
        delsub=courseList.chooseCourse(sem)
        print(delsub)
        while(True):
            print("\n1.Delete course \n2.Back")
            a = int(input("\nEnter choice:\n"))
            if a==1:
                delCourse = input("\nEnter course to delete : \n")
                check=Registrar.toCheck(delCourse)
                if(check<3):
                    if delCourse in delsub:
                        delsub.remove(delCourse)
                        print("""
        * * * * * N O T I F I C A T I O N * * * * *""")
                        print("\nNew course List of the sem : ")
                        print(delsub)
                    else:
                        print("Invalid Input!!")
                else:
                    print("Course Contains more than 3 students")
            elif a==2:
                break 
    
    #10. To Display Student Details
    def displayStudent(std):
        print("\nName : ",std[0],"\nDOB : ",std[1],"\nAddress : ",std[2],"\nCourse : ",std[3])

    #11. To Display Professor Details
    def displayProfessor(prof):
        print("\nName : ",prof[0],"\nSubject : ",prof[1],"\nStudents : ",prof[2])

    #12. To Modify Student Details
    def modifyStudents():
        print("""
        * * * * * M O D I F Y   S T U D E N T * * * * *\n""")
        rollnum=int(input("Enter Roll Number : "))
        std=studDetails.studDetails(rollnum)
        Registrar.displayStudent(std)
        choose = int(input("\nChoose Number to edit : "))
        std[choose-1]=input("Enter the detail : ")
        print("""
        * * * * * U P D A T E D  D E T A I L S * * * * *""")
        Registrar.displayStudent(std)

    #13. To Modify Professor Details
    def modifyProfessors():
        print("""
        * * * * * M O D I F Y   P R O F E S S O R * * * * *\n""")
        id=int(input("Enter Professor ID : "))
        profDetails=DefaultProf()
        prof=profDetails.getProf(id)
        Registrar.displayProfessor(prof)
        choose = int(input("\nChoose Number to edit : "))
        prof[choose-1]=input("Enter the detail : ")
        print("""
        * * * * * U P D A T E D  D E T A I L S * * * * *""")
        Registrar.displayProfessor(prof)

    #14. To Display and Update batch Details for new Batch
    def batchCourse():
        bc=bCourse.getDetails()
        for i in range(0,len(bc)):
            print("\n Semester ",i+1,": ",bc[i])
    
    #15. To Notify Students
    def notify():
        msg=input("Enter the message to notify students : ")
        print("""
        * * * * * N O T I F I C A T I O N * * * * *""")
        print("\nNotify : ",msg,"\n\nMessage send Successfully!!")
    
    #16. Welcome Page
    def exec():
        print("""
        * * * * * W E L C O M E  R E G I S T R A R * * * * *""") 
        while(True):
            print("\nSelect option:")
            print("""
            1.View Students                 7.Freeze Course
            2.View Professors               8.Notify Students
            3.Register Students             9.Modify Student Details
            4.Register Professors           10.Modify Professor Details
            5.Add Course                    11.New Batch
            6.Delete Course                 12.Exit\n""")
            ch = int(input("\nEnter choice:\n"))
            if ch==1:
                Registrar.viewStudent()
            elif ch==2:
                Registrar.viewProfessor()
            elif ch==3:
                Registrar.registerStudent()
            elif ch==4:
                Registrar.registerProfessor()
            elif ch==5:
                Registrar.addCourse()
            elif ch==6:
                Registrar.deleteCourse()
            elif ch==7:
                Registrar.freezeCourse()
            elif ch==8:
                Registrar.notify()
            elif ch==9:
                Registrar.modifyStudents()
            elif ch==10:
                Registrar.modifyProfessors()
            elif ch==11:
                Registrar.batchCourse()
            elif ch==12:
                exit()
            else:
                print("Invalid Choice\n")

reg=Registrar()
profDetails=DefaultProf()
bCourse=BatchCourse()
studDetails=DefaultStud()