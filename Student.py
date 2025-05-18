from DefaultClass import *
from DefaultStudent import *
from Billing import *
from DefaultMarks import *

class Students(DefaultCourse,DefaultStud,Bill):

    #1.Constructor
    def __init__(self):
        super().__init__()

    #2. To select a Course for a particular semester
    def toChoose(sem):
        courselist = DefaultCourse()
        mylist=courselist.chooseCourse(sem)
        return mylist
    
    #3. To print Serial Number
    def inc():
        global count
        count += 1
        return count

    #4. To find Duplicate in the user input
    def findDuplicates(course_list):
        course_list = list(dict.fromkeys(course_list))
        return course_list

    #5. To Select four Courses
    def selectCourse(sem):
        fine=[]
        batchcourse = Students.toChoose(sem)
        input_string = input('\nSelect Primary Course and Secondary Course : ')
        c_list = input_string.split(' ')
        for i in range(0, len(c_list)):
            c_list[i] = int(c_list[i])
        my_list=Students.toChoose(sem)
        course_list=[]
        for i in c_list:
            course_list.append(my_list[i-1])
        selectedCourse=Students.findDuplicates(course_list)
        if(len(selectedCourse)!=4):
            print("\nSelect 4 courses to proceed!!")
            return Students.selectCourse(sem)
        elif(len(selectedCourse)==4):
            fine=selectedCourse
            check =  all(item in batchcourse for item in selectedCourse)
            if check is True:
                print("\nCourse added Successfully\n")    
            else :
                print("\nInvalid course selected")
                return Students.selectCourse(sem)
        return fine

    #6. To convert List to Array
    def listToArr(mylist):
        myCourse=''
        for x in mylist:
            myCourse += str(Students.inc())+'. '+x+' \n'
        global count
        count =0
        return myCourse

    #7. To Display Course list to Students
    def toSelect(sem):
        mylist=Students.toChoose(sem)
        myCourse=Students.listToArr(mylist)
        print("\nChoose four courses from this list:\n\n",myCourse)
        course_list=Students.selectCourse(sem)
        return course_list

    #8. To Display Student's Personal Deatils
    def personalDetails(num):
        ls=stdetail.getDetails()
        student=ls[num]
        print("Student Name : ",student[0])
        print("Date of Birth : ",student[1])
        print("Address : ",student[2])
        return student
     
    #9. To Return Bill Amount
    def returnSum(myDict):
        list = []
        for i in myDict:
            list.append(myDict[i])
        final = sum(list)
        return final

    #10. To Display Subject Price and Bill
    def toBill(clist):
        subject=Bill()
        bill=subject.getBill()
        amount={}
        for x in clist:
            sum=bill[x]
            amount[x]=sum
        print("Subject price : \n")
        Students.displayDetails(amount)
        billAmount=Students.returnSum(amount)
        print("Total : ",billAmount,"\n")
        return billAmount

    #11. To Display a Dictionary
    def displayDetails(test_dict):
        for i in test_dict :
            print(i, test_dict[i])

    #12. To Display Student's Detail
    def viewDetails(num):
        print("""\n
    * * * * * S T U D E N T  D E T A I L * * * * *\n""")
        student=stdetail.studDetails(num)
        print("Student Name : ",student[0])
        print("Date of Birth : ",student[1])
        print("Address : ",student[2])
        print("Subjects : ",student[3])
    
    #13. To Display Report Card
    def displayReport(num):
        print("Name : ",num[0])
        print("Marks")
        test_dict=num[1]
        for i in test_dict :
            print(i, test_dict[i])

    #14. To Display Existing Course List of Student
    def courseUpdate(num):
        print("""\n
    * * * * * C O U R S E  U P D A T E * * * * *\n""")
        course=stdetail.studCourse(num)
        myCourse=Students.listToArr(course)
        print("Student Course : \n",myCourse)
        val=Students.toSelect(num)
        print(val)
        
    #15. To Display Report Card
    def viewReport(num):
        print("""\n
    * * * * * R E P O R T  C A R D * * * * *\n""")
        report=dMarks.grades(num)
        Students.displayReport(report)

    #16. To do Course registration
    def doRegister(num):
        studentDetails={}
        student=Students.personalDetails(num)
        while(True):
            sem=int(input("Enter course semester : "))
            if(sem>0 and sem<9):
                break
            else:
                print("Invalid Input")
        courseSelected=Students.toSelect(sem)
        amount=Students.toBill(courseSelected)
        studentDetails["Name"]=student[0]
        studentDetails["Semester"]=sem
        studentDetails["Course"]=courseSelected
        studentDetails["Bill"]=amount
        Students.displayDetails(studentDetails)
        
    #17. Welcome page
    def exec():
        print("""
    * * * * * W E L C O M E  S T U D E N T * * * * *\n""")
        num=int(input("Enter Student id : "))
        while(True):
            print("\n1.Register\n2.View Details\n3.Course Update\n4.View Report Card\n5.Exit")
            ch = int(input("\nEnter choice:\n"))
            if ch==1:
                Students.doRegister(num)
            elif ch==2:
                Students.viewDetails(num)
            elif ch==3:
                Students.courseUpdate(num)
            elif ch==4:
                Students.viewReport(num)
            elif ch==5:
                print("""
    * * * * * * * * T H A N K  Y O U * * * * * * * *\n""")
                exit()
            else:
                print("\nInvalid Choice !!!")
                
stud=Students()
count=0
dMarks= Mark()
stdetail = DefaultStud()