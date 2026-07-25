# variables
name = "Adithyan"
age = 22
height = 6.1
is_developer = True

# Print them
print(name)
print(age)
print(height)
print(is_developer)

# User input
your_name= input("what is your name?")
your_age= input("how old are you?")
print("hello" + your_name + "! You are" + your_age + " years old.")

#If/Else conditions
age = int(input("Enter your age:"))
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

#Loops
for i in range(5):
    print("Number:", i)

#Lists
fruits = ["apple", "banana", "mango", "orange"]
print(fruits)
print(fruits[0])
print(fruits[2])

for fruit in fruits:
    print(" I Like", fruit)

# Functions
def greet(name):
    print("Hello", name + "! Welcome to python.")

def add_numbers(a, b):
    result = a + b
    print(a, "+", b, "=", result)

greet("Adithyan")
add_numbers(10, 5)
add_numbers(100, 200)