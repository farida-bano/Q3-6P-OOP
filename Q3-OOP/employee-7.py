# 7. Access Modifiers: Public, Private, Protected

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # Public
        self._salary = salary      # Protected
        self.__ssn = ssn           # Private Social Security Number

    def display(self):
        print(self.name)
        print(self._salary)
        print(self.__ssn)  # Accessing within the class

        # Create an Employee object
emp = Employee("Farida Bano", 45000, "123-45-23423")

# Call the display method
emp.display()