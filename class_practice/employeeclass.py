# CREATING AN EMPLOYEE CLASS

# parent class
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

# creating the child class
class SalaryEmployee(Employee): # takes the parent class as perameter
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name) 
        self.salary = salary 

# creating a method to calculate weekly paycheck
    def calculate_paycheck(self):
        return self.salary/52 
    
# creting a different type of employee (hourly paid)

class HourlyEmployee(Employee): # takes parent class as perameter 
    def __init__(self, first_name, last_name, weekly_hours, hourly_rate):
        super().__init__(first_name, last_name)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self):
        return self.weekly_hours * self.hourly_rate
    

# creating a compission employee class that is the child of salary employee class

class ComissionEmployee(SalaryEmployee): # takes SalaryEmployee as parent class in perameters
    def __init__(self, first_name, last_name, salary, sales_num, comission_rate):
        super().__init__(first_name, last_name, salary)
        self.sales_num = sales_num
        self.comission_rate = comission_rate

    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck() # to work out the employees usual salary without comisison
        total_comission = self.sales_num * self.comission_rate # to work out the comission amount
        return regular_salary + total_comission # adds both together 
    