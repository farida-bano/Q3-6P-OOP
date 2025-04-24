# 4. Class Variables and Class Methods

#Assignment:
#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Default Bank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder  # Instance variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Modify the class variable

    def display(self):
        # Corrected f-string formatting to properly display the instance variables
        print(f"Account Holder: {self.account_holder}, Bank: {self.bank_name}")

# Creating two bank accounts
account1 = Bank("Farida")
account2 = Bank("Ahmed")

# Display details for both accounts
account1.display()
account2.display()

# Change the bank name using the class method
Bank.change_bank_name("National Bank of Pakistan")

# Display the updated bank name for both accounts
account1.display()
account2.display()
