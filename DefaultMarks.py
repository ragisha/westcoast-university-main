class Mark():
    def __init__(self):
        #1.Defaullt marklist of each student 
        self.marks = [[],
            ["Aarav",{"Maths":90,"Python":79,"C":80,"Java":81}],
            ["Ahana",{"Maths":88,"C":90,"DBMS":95,"Java":80}],
            ["Bob",{"Maths":76,"OOAD":80,"C":75,"Java":83}],
            ["Charles",{"Maths":93,"Python":77,"DBMS":84,"Java":79}],
            ["Divaker",{"Maths":91,"OOAD":69,"ML":80,"JS":82}],
            ["Ganesh",{"Python":79,"OOAD":62,"AI":69,"JS":80}],
            ["Kishore",{"Python":85,"C":79,"DBMS":90,"ML":74}],
            ["Navin",{"Python":90,"ML":80,"AI":79,"JS":82}],
            ["Pranav",{"Python":91,"ML":90,"AI":84,"JS":98}],
            ["Rahin",{"C":89,"ML":95,"AI":90,"DBMS":87}]]

    #2.Returns marks based on their rollno        
    def grades(self,rollno):
        return self.marks[rollno]