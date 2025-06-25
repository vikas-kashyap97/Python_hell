# conditional statement in Python 

# 1. if statement
#  if statement works only for True condition

a = 26 
b = 108 
if b > a:    # true 
    print("b is greater than a") 

a = 260 
b = 108 
if b > a:    #false - no output 
    print("b is greater than a") 

age = int(input("Enter your age: ")) 
if age > 19:
    print("Your are an adult")
    

# 2. if-else statement
# else handles False condition

age = int(input("Enter your age: ")) 
if age > 19:
    print("Your are an adult")
else:
    print("You are not an adult")

temp = 30 

if temp < 25:
    print("It's a cool day")
else:
    print("It's a hot day") 


# 3. if-elif-else statement 
# multiple conditions 

marks = int(input("Enter your marks-100: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else: 
    print("Grade: C") 


# 4. Nested if-else statement: 
# if-else inside if-else statement 
# multiple conditions depend on each other 

# Q: positive, negative & zero. Postive - even/odd 
number = int(input("Enter a number: "))

if number > 0: #checking positive number 
    if number % 2 == 0:
        print("This is a even number")
    else:
        print("This is an odd number")
else:
    if number == 0: # checking zero value 
        print("This is zero")
    else:
        print("This is a negative number")


# 5. Conditional Expressions (ternary operator)
 
age = int(input("Enter your age: "))
status = "Major" if age >= 18 else "Minor"
print(status)



value = None
if value:
    print("Value is true")
else:
    print("Value is false")
    
    
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")


user_name = "Vikas@1997"
user_password = "12345"
user = input("Enter your username: ")
password = input("Enter your password: ")

if user == user_name and password == user_password:
    print("Login successful")
else:
    if user != user_name:
        print("Invalid username")
    elif password != user_password:
        print("Invalid password")
    else:
        print("Login failed")
        
         
math_marks = int(input("Enter your marks in Mathematics: "))
physics_marks = int(input("Enter your marks in Physics: "))
chemistry_marks = int(input("Enter your marks in Chemistry: "))
total = math_marks + physics_marks + chemistry_marks


if (math_marks >= 65 and physics_marks >= 55 and chemistry_marks >= 50 and total >= 180) or (math_marks + physics_marks >= 140):
    print("You are eligible for admission")
else:
    print("You are not eligible for admission")

