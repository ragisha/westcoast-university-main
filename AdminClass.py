class BatchCourse():
    def __init__(self):
        #1.Course List Maintained by Registrar and is visible only to Registrar
        self.courses = [["Python","Maths","C","DBMS","ML","OOAD","AI","Java","JS","C#","OOPS","CN"],
                ["Maths","C","DBMS","C#","OOPS","CN","ML","OOAD","AI","Java","JS","Python"],
                ["C","DBMS","ML","OOAD","AI","Java","C#","OOPS","CN","JS","Python","Maths"],
                ["DBMS","ML","OOAD","AI","Java","JS","Python","Maths","C","C#","OOPS","CN"],
                ["ML","OOAD","C#","OOPS","CN","AI","Java","JS","Python","Maths","C","DBMS"],
                ["C#","OOPS","CN","OOAD","AI","Java","JS","Python","Maths","C","DBMS","ML"],
                ["AI","C#","OOPS","CN","Java","JS","Python","Maths","C","DBMS","ML","OOAD"],
                ["Java","JS","Python","C#","OOPS","CN","Maths","C","DBMS","ML","OOAD","AI"]]
    #2. Returns the course List
    def getDetails(self):
        return self.courses