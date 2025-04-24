# 9. Abstract Classes and Methods
#Assignment:
#Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Create an instance of Rectangle with width 4 and height 5
rect = Rectangle(4, 5)

# Call the area method to get the area of the rectangle
print(f"The area of the rectangle is: {rect.area()}")  # Output will be 20

