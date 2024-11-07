# CREATING AN EMPLOYEE CLASS

# creating the class
class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary 

# creating a method to calculate weekly paycheck
    def calculate_paycheck(self):
        return self.salary/52 