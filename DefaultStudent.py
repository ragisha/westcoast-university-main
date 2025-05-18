#1.Default student details
class DefaultStud():
    def __init__(self):
        self.subjects = [[],
                ["Aarav","24-07-2000","Chennai,Tamil Nadu",["Maths","Python","C","Java"]],
                ["Ahana","10-05-2000","Thiruvananthapuram,Kerala",["Maths","C","DBMS","Java"]],
                ["Bob","21-01-2000","Bangaluru,Karnataka",["Maths","OOAD","C","Java"]],
                ["Charles","29-03-2000","Srinagar,Jammu",["Maths","Python","DBMS","Java"]],
                ["Divaker","29-02-2000","Thiripura,Agarthala",["Maths","OOAD","ML","JS"]],
                ["Ganesh","31-12-2001","Panaji,Goa",["Python","OOAD","AI","JS"]],
                ["Kishore","12-12-2001","Gandhinagar,Gujarath",["Python","C","DBMS","ML"]],
                ["Navin","04-09-2001","Chandigarh,Punjab",["Python","ML","AI","JS"]],
                ["Pranav","07-07-2001","Amaravathi,Andra Pradesh",["Python","ML","AI","JS"]],
                ["Rahin","04-09-2001","Hyderabad,Telangana",["C","ML","AI","DBMS"]]]

    #2.Returns students data based on rollno
    def studDetails(self,rollno):
        return self.subjects[rollno]

    #3.Returns subjects selected by the student
    def studCourse(self,rollno):
        return self.subjects[rollno][3]
        
    #4.Returns the whole student details list
    def getDetails(self):
        return self.subjects
   


