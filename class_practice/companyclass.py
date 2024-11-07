# CREATING A COMPANY CLASS TO GO ALONG WITH EMPLOYEE CLASS

from employeeclass import Employee, SalaryEmployee, HourlyEmployee, ComissionEmployee # imprting the employee class from employeeclass.py

class Company:
    def __init__(self):
        self.employees = [] # defines employees as an empty list 
    
    def add_employee(self, new_employee):
        self.employees.append(new_employee) # adds the new employee to the employees list

    def display_employees(self):
        print("Current employees:")
        for i in self.employees:
            print(i.first_name, i.last_name)
        print("-----------------") # to indicate that is the end of the list 

    def pay_employees(self):
        print("Paying Employees:")
        for i in self.employees:
            print(f"Paycheck for {i.first_name} {i.last_name}")
            print(f"Amount: £{i.calculate_paycheck():,.2f}") #:.,2f rounds the float to 2 decimal places
            print("----------------")

def main():
    my_company = Company()

    employee1 = SalaryEmployee("Eloise", "Wilkinson", 41000) # salary employee
    my_company.add_employee(employee1)

    employee2 = HourlyEmployee("Dominic", "Morton-Smith", 25, 50) # hourly rate employee - calling the first name, last name, hours worked and hourly rate
    my_company.add_employee(employee2)

    employee3 = ComissionEmployee("Harry", "Styles", 30000, 5, 200) # comission employee - calling slary amount, sales amoutn and comission rate 
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()



# Ensure that the main function is called when the script is executed
if __name__ == "__main__":
    main()