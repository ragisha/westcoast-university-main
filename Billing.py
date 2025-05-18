#1.Billing of the course selected by student
class Bill():
    def __init__(self):
        #2.Course and their amount
        self.rate={
        "Python":40,
        "Maths":30,
        "C":35,
        "DBMS":25,
        "ML":35,
        "OOAD":40,
        "AI":35,
        "Java":45,
        "JS":30}
    #3.Returns Billing value
    def getBill(self):
        return self.rate
