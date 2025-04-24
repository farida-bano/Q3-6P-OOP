# 10. Instance Methods
#Assignment:
#Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

# Create an instance of the Dog class
my_dog = Dog("Rex", "German Shepherd")

# Call the bark method on the instance
my_dog.bark()
