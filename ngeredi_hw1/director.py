from BaseEmployee import Employee

class Director(Employee):
    def __init__(self, employee_id, first_name, last_name, email, salary, department, bonus):
        super().__init__(employee_id, first_name, last_name, email, salary)
        self.department=department
        self.bonus=bonus
    def calculateBonus(self):
        directorSalary= self.getEmployeeSalary()+self.bonus
        return f'The new salary is {directorSalary} $\n'

objdorector=Director(3,'Dianne','Mugunga','dmugunga@gmail.com', 520000,'security department',60000)
objdorector.calculateBonus()
objdorector.employeeIformation()
print(objdorector.calculateBonus())