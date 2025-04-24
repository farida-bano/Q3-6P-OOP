#2. Using cls

#Assignment:
#Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Objects created: {cls.count}")

    # Optionally, adding a __str__ method to display the instance count
    def __str__(self):
        return f"Counter Object (ID: {id(self)})"

# Creating counter objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()
# Display the total count of objects created
Counter.display_count()