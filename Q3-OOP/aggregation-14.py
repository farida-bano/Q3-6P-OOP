#14. Aggregation
#Assignment:
#Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class EmployeeAgg:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Department:
    def __init__(self, name, employees):
        self.name = name
        # employees is expected to be a list of EmployeeAgg objects
        self.employees = employees

    def show_employees(self):
        print(f"Employees in the {self.name} department:")
        for employee in self.employees:
            print(employee)

# Create some EmployeeAgg objects
employee1 = EmployeeAgg("Farida")
employee2 = EmployeeAgg("Erum")
employee3 = EmployeeAgg("Alishba")

# Create a Department object and pass in the EmployeeAgg objects as a list
department = Department("HR", [employee1, employee2, employee3])

# Call the method to show employees in the department
department.show_employees()