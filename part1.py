from datetime import date
def defaultCourse(sem):
        if sem ==1:
            sem_one=["Physics1","Maths1","English","Chemistry1","Python","EG"]
            return sem_one
        elif sem == 2:
            sem_two=["Physics2","Maths2","English","Chemistry2","C","BEEE"]
            return sem_two
        elif sem == 3:
            sem_three=["Maths3","Java","CE","DPSD","PHP","Environment Science"]
            return sem_three
        elif sem == 4:
            sem_four=["Computer Architecture","Maths4","Data Structure","OOPS","C++","DBMS"]
            return sem_four
        elif sem == 5:
            sem_five=["Computer Networks","Maths5","Design Analysis of Algorithm","Chemistry2","Operating System","Internet Programming"]
            return sem_five
        elif sem == 6:
            sem_six=["Mobile Computing","Maths2","Theory of Computing","Ethics","OOAD","Artificial Intilegence"]
            return sem_six
        elif sem == 7:
            sem_seven=["Software Testing","GIS","Compiler Design","Cloud Computing","RPA","Machine Learning"]
            return sem_seven
        elif sem == 8:
            sem_eight=["Hospital Management","Information retrivel","C#","Ecosystem","Hadoop","Nutrition"]
            return sem_eight

def courselist(sem):
    batchcourse=defaultCourse(sem) #admin course
    # todays_date = date.today()
    # if(todays_date.year<yoj):
    #     batchcourse=defaultCourse(sem)
    return batchcourse
def findDuplicates(course_list):
    course_list = list(dict.fromkeys(course_list))
    return course_list
def selectCourse(sem):
    fine=[]
    batchcourse = courselist(sem)
    input_string = input('Select Course : ')
    course_list = input_string.split(',')
    selectedCourse=findDuplicates(course_list)
    if(len(selectedCourse)!=4):
        print("Select 4 courses to proceed!!")
        return selectCourse(sem)
    elif(len(selectedCourse)==4):
        fine=selectedCourse
        check =  all(item in batchcourse for item in selectedCourse)
        if check is True:
            print("Course added Successfully")    
        else :
            print("Invalid course selected")
            return selectCourse(sem)
    return fine
def student():
    studentDetails={}
    print("* * * * * W E L C O M E * * * * *")
    name=input("Enter Student name : ")
    dob=input("Enter date of birth : ")
    yoj=int(input("Enter year of joining : "))
    # year=int(input("Enter course year : "))
    while(True):
        sem=int(input("Enter course semester : "))
        if(sem>0 and sem<9):
            break
        else:
            sem=int(input("Enter course semester : "))
    address=input("Enter Student address : ")
    print("Choose four courses from this list:",courselist(sem))
    course_list=selectCourse(sem)
    studentDetails["name"]=name
    studentDetails["dob"]=dob
    studentDetails["yoj"]=yoj
    # studentDetails["year"]=year
    studentDetails["semester"]=sem
    studentDetails["address"]=address
    studentDetails["course"]=course_list
    print(studentDetails)
student()
