from BaseEmployee import Employee

class Intern(Employee):
    def __init__(self, employee_id, first_name, last_name, email, salary, universityName, programName,internshipDuration,):
        super().__init__(employee_id, first_name, last_name, email, salary)
        self.niversityName=universityName
        self.programNamne=programName
        self.internshipDuration=internshipDuration
    def internEarngs(self):
        internSalary=(self.getEmployeeSalary()*self.internshipDuration)/12
        return f'The new intern Salary is {internSalary} $\n'
    
objintern=Intern(100, 'Christine', 'Ingabire', 'ingabirec@gmail.com',50000,'University of Rwanda', 'ETE',3)
objintern.employeeIformation()
print(objintern.internEarngs())