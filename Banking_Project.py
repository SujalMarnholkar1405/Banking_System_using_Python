#Banking System 
class Person:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.address = input("Enter your address: ")
        self.phone_number = input("Enter your phone number: ")

    def display_personal_info(self):
        print("\n--- Personal Info ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")

class Account:
    def __init__(self):
        self.account_number = input("Enter your Account Number: ")
        self.balance = 0
        self.account_type = input("Enter Account Type (Savings/Current): ")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def display_account_info(self):
        print("\n--- Account Info ---")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ₹{self.balance}")

class Customer(Person, Account):
    def __init__(self):
        print("Opening Customer Profile...")
        Person.__init__(self)
        Account.__init__(self)

    def open_account(self):
        print("Account opened successfully!")

    def close_account(self):
        print("Account closed. Balance refunded: ", self.balance)
        self.balance = 0

    def update_account_info(self):
        print("Updating Account Info...")
        self.address = input("Enter new address: ")
        self.phone_number = input("Enter new phone number: ")
        print("Information updated!")


class BankManager(Person):
    def __init__(self):
        super().__init__()
        self.employee_id = input("Enter Employee ID: ")
        self.position = input("Enter Position (Manager/Senior Manager): ")

    def approve_loan(self):
        print(f"Loan approved by {self.position}.")

    def manage_accounts(self):
        print("Managing accounts...")

    def display_manager_info(self):
        self.display_personal_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")

print("Creating Customer...\n")
cust = Customer()
cust.display_personal_info()
cust.display_account_info()

cust.deposit(int(input("Enter Value for deposite")))
cust.withdraw(int(input("Enter Value for withdraw")))
cust.check_balance()


print("\nCreating Bank Manager...\n")
mgr = BankManager()
mgr.display_manager_info()

