# CREATING A COMPANY CLASS TO GO ALONG WITH EMPLOYEE CLASS

from employeeclass import Employee # imprting the employee class from employeeclass.py

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

    employee1 = Employee("Eloise", "Wilkinson", 41000)
    my_company.add_employee(employee1)

    employee2 = Employee("Dominic", "Morton-Smith", 45000)
    my_company.add_employee(employee2)

    employee3 = Employee("Harry", "Styles", 100000)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()



# Ensure that the main function is called when the script is executed
if __name__ == "__main__":
    main()