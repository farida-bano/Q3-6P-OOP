# 18. Property Decorators
# Assignment:
#Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# Example usage:
product = Product(100)  # Initialize with price 100

# Accessing the price using the getter
print("Initial Price:", product.price)

# Changing the price using the setter
product.price = 150
print("Updated Price:", product.price)

# Deleting the price using the deleter
del product.price

# Trying to access the price after deletion (this will raise an AttributeError)
try:
    print("Price after deletion:", product.price)
except AttributeError as e:
    print("Error:", e)
