#1. Define a class which has at least two methods one, to get a string 
#from console  input and other is to print the string in uppercase.
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def get_input(self):
        self.input_string = input("Enter a string: ")

    def print_uppercase(self):
        if self.input_string:
            print("Uppercase String:", self.input_string.upper())
        else:
            print("No input string provided.")

# Create an instance of the class
string_manipulator = StringManipulator()

# Get input from the user
string_manipulator.get_input()

# Print the input string in uppercase
string_manipulator.print_uppercase()
#2. Define a class, which have a class parameter and have a same instance 
#parameter.
class MyClass:
    param = None  # Class parameter (class attribute)

    def __init__(self, param):
        self.param = param  # Instance parameter (instance attribute)

# Create instances of the class with different values for 'param'
obj1 = MyClass("Instance 1")
obj2 = MyClass("Instance 2")

# Access class parameter and instance parameter for both instances
print("Class parameter:", MyClass.param)
print("Instance 1 parameter:", obj1.param)
print("Instance 2 parameter:", obj2.param)
#3. Define a class named Circle which can be constructed by radius.
# The Circle class has a method which can compute the area.
class Circle:
    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    def compute_area(self):
        pi = 3.14159265359  # Approximate value of pi
        area = pi * (self.radius ** 2)  # Compute the area using the formula πr^2
        return area

# Create an instance of the Circle class with a radius of 5 units
circle = Circle(5)

# Compute and print the area of the circle
area = circle.compute_area()
print("Area of the circle:", area)
#4. Define a class named BankAccount. This class should contain
#  methods withdraw() and deposit to calculate the balance amount remained 
#  in your account.
class BankAccount:
    def __init__(self):
        self.balance = 0  # Initialize the balance to zero

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")
        else:
            print("Insufficient balance for withdrawal.")

# Create an instance of the BankAccount class
account = BankAccount()

# Deposit $100 into the account
account.deposit(100)

# Withdraw $50 from the account
account.withdraw(50)

# Try to withdraw an invalid amount and an amount exceeding the balance
account.withdraw(200)
account.withdraw(-10)

# Deposit another $75
account.deposit(75)
#5.Define a class named Shape and its subclass Square.the Square class 
# has an init function which takes a length as argument. Both classes
# have a area function which can print the area of the shape where 
# Shape's area is 0 by default. 


class Shape:
    def area(self):
        return 0  # Default area for the base Shape class

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2  # Area of a square is length * length

# Create instances of the Shape and Square classes
shape = Shape()
square = Square(4)  # Creating a square with a side length of 4

# Calculate and print the areas
print("Area of the generic shape:", shape.area())  # Calls the base class method (0 by default)
print("Area of the square:", square.area())  # Calls the overridden method (16 for a 4x4 square)
