from DefaultClass import *
from DefaultStudent import *
from DefaultProfessor import *
from DefaultMarks import *
class Professors(DefaultCourse,DefaultStud,DefaultProf):
    #1.Calls the parent constructor
    def __init__(self):
        super().__init__()

    #2.Displays the subject the Professor teaches and also allows them to choose a subject they wish to teach
    def doTeach(ls,profid):
        professorDetails={}
        teachingsub=ls[profid]
        print("The course you are teaching currently is ",teachingsub[1])
        while(True):
            sem=int(input("Enter course semester : "))
            if(sem>0 and sem<9):
                break
            else:
                sem=int(input("Enter course semester : "))
        courselist=DefaultCourse()
        clist=courselist.chooseCourse(sem)
        print("Choose any one course from this list:\n",clist)
        input_string = int(input('Select Course : '))
        ls[profid][1]=clist[input_string-1]
        print("Updated Course: ", ls[profid][1])
    
    #3.Prints the students names who opted for a subject handled by professor based on professor ID
    def studentDetails(ls,profid):
        professor=ls[profid]
        print("\nStudents who opted the subject:\n")
        for x in professor[2]:
            print("\n",x)

    #4.Prints the students Grade with their name
    def displayReport(mark):
        print("\nName : ",mark[0])
        print("\nMarks :\n")
        test_dict=mark[1]
        for i in test_dict :
            print(i," : ", test_dict[i])

    #5.Displays report card by using rollno and calls the above method to print them
    def reportCard(ls,std,profid):
        rollno=int(input("Enter Student RollNo : "))
        professor=ls[profid]
        stud=professor[2]
        profDetails=DefaultProf()
        names=profDetails.studName(profid)
        defMarks=Mark()
        mark=defMarks.grades(rollno)
        print("\n * * * * * R E P O R T  C A R D * * * * *\n")
        for x in stud:
            if x in mark[0]:
                Professors.displayReport(mark)
    
    #6.This method gets executed first
    def exec():
        print("* * * * * W E L C O M E  P R O F E S S O R * * * * *")
        while(True):

            #7.Professor Id input given by user
            profid=int(input("Enter Professor ID : "))
            if profid>9 or profid<0:
                print("Invalid ID")
            else:
                profDetails=DefaultProf()
                ls=profDetails.getDetails()
                print("Welcome Professor ",ls[profid][0],"!!")
                studDetails=DefaultStud()
                std=studDetails.getDetails()

                #8.Switch Case options to select a course to teach, view students details and also view their report cards
                while(True):
                    print("\nSelect option:")
                    print("\n1.Course to Teach \n2.View Student Details\n3.View Report Card\n4.Exit")
                    ch = int(input("\nEnter choice:\n"))
                    if ch==1:
                        Professors.doTeach(ls,profid)
                    elif ch==2:
                        Professors.studentDetails(ls,profid)
                    elif ch==3:
                        Professors.reportCard(ls,std,profid)
                    elif ch==4:
                        print("""
    * * * * * * * * T H A N K  Y O U * * * * * * * *\n""")
                        exit()
                    else:
                        print("\nInvalid Choice !!!")

prof=Professors()