"""Problem Statement 1: Employee Management System*
Design a Python program to manage employee details in an organization.  
1. Create a class Employee with attributes:
   - name (string): Name of the employee.  
   - employee_id (integer): Unique ID for the employee.  
   - salary (float): Monthly salary of the employee.  

2. Add a method calculate_annual_salary() to calculate and return the annual salary of the employee.

*Example*:  
Input: Employee("John Doe", 101, 50000)  
Output: Annual Salary of John Doe is ₹600000

"""


class Employee:
    def details(self):
        self.name=str(input("name of the employee "))
        self.id = int(input("enter id "))
        self.sal = float(input("monthly salary "))


    def annual_salary(self):
        annual = self.sal * 12
        print(annual)


a1= Employee()
a1.details()
a1.annual_salary()

