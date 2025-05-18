from AdminClass import *
class DefaultCourse(BatchCourse):

    #1.Course list provided to student to choose their course
    def __init__(self):
        self.subjects = [["Python","Maths","C","DBMS","ML","OOAD","AI","Java","JS","C#"],
                         ["Maths","C","DBMS","ML","OOAD","AI","Java","JS","Python","C#"],
                         ["C","DBMS","ML","OOAD","AI","Java","JS","Python","Maths","C#"],
                         ["DBMS","ML","OOAD","AI","Java","JS","Python","Maths","C","C#"],
                         ["ML","OOAD","AI","Java","JS","Python","Maths","C","DBMS","C#"],
                         ["OOAD","AI","Java","JS","Python","Maths","C","DBMS","ML","C#"],
                         ["AI","Java","JS","Python","Maths","C","DBMS","ML","OOAD","C#"],
                         ["Java","JS","Python","Maths","C","DBMS","ML","OOAD","AI","C#"]]

    #2.Returns the course list for each semester
    def chooseCourse(self,sem):
        return self.subjects[sem-1]

    #3.Course list updated batch wise
    def batchUpdate(self):
        super().__init__()
        student=bc.getDetails()
        return student
bc=BatchCourse()
