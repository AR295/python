# --------while loop 
print("\n----while loop---")
count = 0
while count < 3:
    count = count + 1 
    print("Hello Geek")
print()

# while loop practice by printing table
num = int(input("Enter number you want to display table: "))
i = 1
while i < 11:
    print(i, " * ", num, " = ", i * num)
    i += 1

# -------for loop
print("\n----for loop traversal using list----")
ai = ['robotics', 'deep learning', 'automation']
for item in ai:  # Use a more descriptive variable name like 'item'
    print(item)
print("")

print("\n----for loop traversal by index of sequence----")
li = ['windows', 'linux', 'macOS']
for index in range(len(li)):
    print(index)
print("")

# for loop with break and continue statement
br = int(input("For Loop will display 1 to 10 numbers, enter number at which you want to exit from loop b/w 1 to 10: "))
for i in range(1, 11):  # Adjusted range to include 10
    print(i)
    if i == br:
        break
print("")

con = int(input(f"Enter any number and For Loop will display only even numbers range from 1 to your entered number: "))
for i in range(1, con + 1):  # Adjusted range to include 'con'
    if i % 2 != 0:
        continue
    print(i)
print("")

# ------function
print("\n-----Functions-----")
def display():
    """Function to display a message."""
    print("Programming makes life easy!!!")

display()  # Function call

# function using parameters and return
def sum(num1, num2):
    """Function to sum two numbers."""
    return num1 + num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Sum of {num1} + {num2}: ", sum(num1, num2))

# function with keyword argument
name = input("Enter your name: ")
def greeting(name, greeting="have a nice day!!!"):
    """Function to greet with optional message."""
    print(f"{name} {greeting}")
print()

greeting(name)

# function finding factorial
def factorial(value):
    """Recursive function to calculate factorial."""
    if value < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if value == 1 or value == 0:
        return 1
    return value * factorial(value - 1)

value = int(input("Enter number for factorial: "))
print(factorial(value))

# ---- class 
print("\n-----class------")
class AI:
    """Simple class demonstrating a string."""
    str = "Classes are parts of Object Oriented Programming."

obj = AI()
print(obj.str)

# class with __init__ function which acts as constructor of class
class Person:
    """Class to represent a person."""
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

na = input("Enter your name: ")
ag = int(input(f"Enter {na}'s age: "))
co = input(f"Enter {na}'s country name: ")
p1 = Person(na, ag, co)
print(f"{p1.name} is {p1.age} years old and lives in {p1.country}.\n")

# class with methods
class Room:
    """Class representing a room with methods."""
    length = 0.0
    breadth = 0.0
    
    def calculate_area(self):
        """Method to calculate the area of the room."""
        print("Area of Room =", self.length * self.breadth)

# create object of Room class
study_room = Room()

# assign values to all the properties 
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
study_room.length = l
study_room.breadth = b

# access method inside class
study_room.calculate_area()
