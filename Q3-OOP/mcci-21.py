# 21. Make a Custom Class Iterable
# Countdown class that makes it an iterable
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

# Testing the Countdown class
countdown = Countdown(5)

# Collecting the output from the Countdown iterable
output = list(countdown)
print(output)
