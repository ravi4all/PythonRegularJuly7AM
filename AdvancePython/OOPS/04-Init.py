class Employee:

    # Constructor
    def __init__(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept
        self.company = "TCS"
        self.data = []
        print("Object Constructed for...",self.name)

    def storeEmp(self):
        self.data.append([self.id, self.name, self.dept])
        print(self.data)

    def showEmp(self):
        print("Employee Details : ", self.id, self.name, self.dept, self.company)

    def __del__(self):
        print("Object Destroyed for :",self.name)

e1 = Employee(101,"Ram","IT")
# e1.id = 101
# e1.name = "Ram"
# e1.dept = "IT"
# print("Employee Details : ",e1.id, e1.name, e1.dept, e1.company)
e1.storeEmp()
e1.showEmp()

del e1

e2 = Employee(102,"Shyam","HR")
# e2.id = 102
# e2.name = "Shyam"
# e2.dept = "IT"
# print("Employee Details : ",e2.id, e2.name, e2.dept, e2.company)
e2.storeEmp()
e2.showEmp()


