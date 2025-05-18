class DefaultProf():
    def __init__(self):
        #1.Default Professor list
        self.details=[[],
             ["Divya","Python",["Aarav","Charles","Ganesh","Kishore","Navin","Pranav"]],
             ["David","Maths",["Aarav","Ahana","Bob","Charles","Divaker"]],
             ["Amir","C",["Aarav","Ahana","Bob","Kishore","Rahin"]],
             ["Ravi","DBMS",["Ahana","Charles","Kishore","Rahin"]],
             ["Geetha","ML",["Divaker","Kishore","Navin","Pranav","Rahin"]],
             ["Vijayan","OOAD",["Bob","Divaker","Ganesh"]],
             ["Raji","AI",["Ganesh","Navin","Pranav","Rahin"]],
             ["Govind","Java",["Aarav","Ahana","Bob","Charles"]],
             ["Viji","JS",["Divaker","Ganesh","Navin","Pranav"]],
             ]

        #2.Default Professor list used for deletion
        self.delProf=[
             ["Divya","Python",["Aarav","Charles","Ganesh","Kishore","Navin","Pranav"]],
             ["David","Maths",["Aarav","Ahana","Bob","Charles","Divaker"]],
             ["Amir","C",["Aarav","Ahana","Bob","Kishore","Rahin"]],
             ["Ravi","DBMS",["Ahana","Charles","Kishore","Rahin"]],
             ["Geetha","ML",["Divaker","Kishore","Navin","Pranav","Rahin"]],
             ["Vijayan","OOAD",["Bob","Divaker","Ganesh"]],
             ["Raji","AI",["Ganesh","Navin","Pranav","Rahin"]],
             ["Govind","Java",["Aarav","Ahana","Bob","Charles"]],
             ["Viji","JS",["Divaker","Ganesh","Navin","Pranav"]],
             ["Bala","OOPS",["A","B","C","D","E","F","G","H","I","J"]]]

    #3.Returns Students name under the Professor
    def studName(self,profid):
        return self.details[profid][2]

    #4.Returns Professor Details
    def getDetails(self):
        return self.details

    #5.Returns Professor Details based on their ID
    def getProf(self,id):
        return self.details[id]

    #6.Returns Professor list for deletion
    def delDetails(self):
        return self.delProf