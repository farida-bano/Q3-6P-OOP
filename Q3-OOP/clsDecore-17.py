# 17. Class Decorators
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class PersonWithGreeting:
    def __init__(self, name):
        self.name = name

# Create an instance of PersonWithGreeting
person = PersonWithGreeting("Farida")

# Call the greet method added by the decorator
print(person.greet())  # Output: Hello from Decorator!