class Employee():
    def __init__(self, employee_id, first_name,last_name ,email,salary):

        self.employee_id=employee_id
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.salary=salary
    def employeeIformation(self):
        print(f"\nEmployer Id: , {self.employee_id} $")
        print("Employer first name: ", self.first_name)
        print("Employer last name: ", self.last_name)
        print("Employer email: ", self.email)
        print(f"Employer salary: , {self.salary} $ ")
        # print("\n")
        # print('New Salary is )
    def calculateEarningReturn(self):
        return self.salary

    def getEmployeeID(self):
        return self._employee_id
    def setEmployeeID(self, employee_id):
        self._employee_id=employee_id
    def getEmployeeFirstName(self):
        return self._first_name
    def seEmployeeFirstName(self, first_name):
        self._first_name=first_name
    def getEmployeelastName(self):
        return self._last_name
    def setEmployeelasttName(self, last_name):
        self._last_name=last_name
    def getEmployeeEmail(self):
        return self._email
    def setEmployeeEmail(self, email):
        self._email=email
    def getEmployeeSalary(self):
        return self.salary
    def setEmployeeSalary(self, salary):
        self._salary=salary

    
        
    

objemployee=Employee(23,'Geredi', 'NIYIBIGIRA', 'ngeredi@andrew.cmu.edu', 650000)
# print(objemployee.calculateEarningReturn())
# print(objemployee)
# objemployee.employeeIformation()



#Token git"" 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"

