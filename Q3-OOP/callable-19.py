# 19. callable() and __call__()
# assignment
#Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

# Create an instance of Multiplier with a factor of 3
multiply_by_3 = Multiplier(3)

# Use the __call__ method by calling the object as a function
result = multiply_by_3(5)  # Should multiply 5 by 3

print(result)
