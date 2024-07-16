# Question 1: Numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
print("Question number 1:\nNumbers which are divisible by 7 and multiple of 5, between 1500 and 2700")
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

# Question 2: Temperature conversion between Fahrenheit and Celsius based on user choice
print("\nQuestion number 2:\nTemperature conversion between Fahrenheit and Celsius")
choice = int(input("Enter 1 to convert Fahrenheit to Celsius or Enter 2 to convert Celsius to Fahrenheit: "))
if choice == 1:
    fah = int(input("Enter temperature in Fahrenheit: "))
    cel = 5 * (fah - 32) / 9
    print("Temperature in Celsius: ", int(cel))
elif choice == 2:
    cel = int(input("Enter temperature in Celsius: "))
    fah = 9 * cel / 5 + 32
    print("Temperature in Fahrenheit: ", fah)
else:
    print("Invalid Choice!!!")

# Question 3: Number guessing game
print("\nQuestion number 3:\nNumber guessing game")
import random
num = random.randint(1, 9)
while True:
    guess = int(input("Guess any number between 1 to 9: "))
    if num == guess:
        print("Well guessed!")
        break
    else:
        print("Try again!!!\n")

# Question 4: Pattern printing
print("\nQuestion number 4:\nPattern printing")
star = 6
for i in range(star):
    for j in range(i):
        print("*", end="")
    print()
for i in range(star, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Question 5: Reverse a word
print("\nQuestion number 5:\nReverse a word")
word = input("Enter a word: ")
print(word[::-1])

# Question 6: Count even and odd numbers in a tuple
print("\nQuestion number 6:\nCount even and odd numbers in a tuple")
user_input = input("Enter space separated integers (e.g., 20 3 18): ")
my_tuple = tuple(int(item) for item in user_input.split())
even = sum(1 for x in my_tuple if x % 2 == 0)
odd = len(my_tuple) - even
print("Number of even numbers:", even, "\nNumber of odd numbers:", odd)

# Question 7: Append elements to a list and print their types
print("\nQuestion number 7:\nAppend elements to a list and print their types")
my_list = []
no = int(input("Enter number of elements you want to enter in list: "))
for i in range(no):
    value = input("Enter element: ")
    my_list.append(value)
for item in my_list:
    print(item, " ", type(item))

# Question 8: Print numbers except 3 and 6
print("\nQuestion number 8:\nPrint numbers except 3 and 6")
for x in range(7):
    if x == 3 or x == 6:
        continue
    else:
        print(x, end=" ")

# Question 9: Fibonacci series up to 50
print("\nQuestion number 9:\nFibonacci series up to 50")
num1, num2 = 1, 1
print(num1, num2, end=" ")
while True:
    total = num1 + num2
    if total > 50:
        break
    print(total, end=" ")
    num1, num2 = num2, total

# Question 10: FizzBuzz program
print("\nQuestion number 10:\nFizzBuzz program")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Question 11: Create and print a 2D array
print("\nQuestion number 11:\nCreate and print a 2D array")
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
arr = [[i * j for j in range(n)] for i in range(m)]
for row in arr:
    print(" ".join(map(str, row)))

# Question 12: Convert input to lowercase
print("\nQuestion number 12:\nConvert input to lowercase")
line = input("Enter sequence of lines and press enter to terminate: ")
print(line.lower())

# Question 13: Validate binary numbers and print those divisible by 5
print("\nQuestion number 13:\nValidate binary numbers and print those divisible by 5")
my_list = []
while True:
    num = input("Enter a four-digit binary number: ")
    if len(num) != 4 or not all(bit in '01' for bit in num):
        print("Invalid input! Please enter a valid four-digit binary number.")
        continue
    my_list.append(num)
    choice = input("Enter 1 to add more numbers or 2 to terminate: ")
    if choice != '1':
        break
for binary in my_list:
    decimal_number = int(binary, 2)
    if decimal_number % 5 == 0:
        print(binary, end=" ")

# Question 14: Count digits and letters in a string
print("\nQuestion number 14:\nCount digits and letters in a string")
user_string = input("Enter any string: ")
digits = sum(1 for char in user_string if char.isdigit())
letters = sum(1 for char in user_string if char.isalpha())
print(f"Letters: {letters}\nDigits: {digits}")

# Question 15: Validate password based on given criteria
print("\nQuestion number 15:\nValidate password based on given criteria")
password = input("Enter your password that meets the following criteria:\n"
                 "- At least 1 letter between [a-z] and 1 letter between [A-Z]\n"
                 "- At least 1 number between [0-9]\n"
                 "- At least 1 character from [$#@]\n"
                 "- Minimum length 6 characters\n"
                 "- Maximum length 16 characters\n")
if any(char.islower() for char in password) and any(char.isupper() for char in password) \
        and any(char.isdigit() for char in password) and any(char in '$#@' for char in password) \
        and 6 <= len(password) <= 16:
    print("Valid password")
else:
    print("Invalid password. Please ensure it meets all criteria.")
