from BaseEmployee import Employee
class Manager(Employee):
    def __init__(self, employee_id, first_name, last_name, email, salary,department,numberOfDirect_report, earningRate):
        
        super().__init__(employee_id, first_name, last_name, email, salary)
        self.numberOfDirect_report=numberOfDirect_report
        self.department=department
        self.earningRate=earningRate
    def earnmanager(self):
        # self.amount=amount
        managerSalary=self.getEmployeeSalary()+self.getEmployeeSalary()*(self.earningRate)/100
        # self.setEmployeelasttName('Niyibigira')
        return f'The new salary is {managerSalary} $\n'
    


objmanager=Manager(2, 'Odile','Nzambaza','nzamba@gmail.com', 400000, 'IT Department', 500, 5)
objmanager.employeeIformation()
print(objmanager.earnmanager())