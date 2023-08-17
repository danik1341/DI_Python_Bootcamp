# Data Types

# 1) - C - Tuples

# Lists and Loops

# 1)

squares_of_evens = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(squares_of_evens)
print('/////////////////////////////////////////')

# 2)

divisible_by_both = [num for num in range(1, 11) if num % 2 == 0 and num % 3 == 0]
print(divisible_by_both)
print('/////////////////////////////////////////')

# 3)

student_list = [
    {
    "name": "John", 
    "age": 24
    }, 
    {
    "name": "Anna", 
    "age": 22
    }, 
    {
    "name": "Mike", 
    "age": 25
    }
]

for student in student_list:
    print(f"Name: {student['name']}, Age: {student['age']}")
print('/////////////////////////////////////////')

# Function Behavior with *args and **kwargs

# 1)

def combine_words(*args, **kwargs):
    words = list(args) + list(kwargs.values())
    return " ".join(words)

result = combine_words("Hello", "world", first="Python", second="is", third="great!")
print(result)
print('/////////////////////////////////////////')

# Object-Oriented Programming (OOP)

# 1)

class Vehicle:
    def __init__(self, type: str, brand: str, year: int):
        self.type = type
        self.brand = brand
        self.year = year
        
    def __str__(self):
        return f"Type: {self.type}, Brand: {self.brand}, Year: {self.year}"

vehicle1 = Vehicle("Car", "Toyota", 2020)
vehicle2 = Vehicle("Motorcycle", "Honda", 2018)

print(vehicle1)
print(vehicle2)
print('/////////////////////////////////////////')

# OOP Inheritance and Decorators

class Car:
    def __init__(self, brand: str, model: str, mileage: int):
        self.brand = brand
        self.model = model
        self.mileage = mileage
        
    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Mileage: {self.mileage}"

class ElectricCar(Car):
    def __init__(self, brand, model, mileage, battery_capacity: float):
        super().__init__(brand, model, mileage)
        self._battery_capacity = battery_capacity
        
    @property
    def battery_capacity(self):
        return self._battery_capacity
    
    @battery_capacity.setter
    def battery_capacity(self, value):
        if value > 0:
            self._battery_capacity = value
        
    def __str__(self):
        return f"{super().__str__()}, Battery Capacity: {self._battery_capacity} kWh"

car1 = Car("Toyota", "Camry", 30000)
electric_car1 = ElectricCar("Tesla", "Model S", 15000, 75.5)

print(car1)
print(electric_car1)

electric_car1.battery_capacity = 80.0
print(electric_car1)
print('/////////////////////////////////////////')

# 3)

class BankAccount:
    _total_accounts = 0
    
    def __init__(self, account_holder: str, initial_balance=0.0):
        self._balance = initial_balance
        self._account_holder = account_holder
        BankAccount._total_accounts += 1
        
    @property
    def account_holder(self):
        return self._account_holder
    
    @property
    def balance(self):
        return self._balance
    
    @classmethod
    def total_accounts(cls):
        return cls._total_accounts
    
    @staticmethod
    def bank_policy_message():
        return "Thank you for choosing our bank. Now cough up the dough punk."
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposit successful. New balance: {self._balance}"
        else:
            return "Invalid deposit amount."
        
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            return f"Withdrawal successful. New balance: {self._balance}"
        else:
            return "Insufficient balance or invalid withdrawal amount."
        
    def view_balance(self):
        return f"Account holder: {self._account_holder}, Balance: {self._balance}"

account1 = BankAccount("Alice", 1000.0)
account2 = BankAccount("Bob")

print(account1.deposit(500))
print(account1.withdraw(300))
print(account1.view_balance())

print(account2.deposit(200))
print(account2.withdraw(50))
print(account2.view_balance())

print("Total accounts:", BankAccount.total_accounts())
print(BankAccount.bank_policy_message())
print('/////////////////////////////////////////')
