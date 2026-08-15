# Task 1
marks = int(input("Enter the marks:"))
if marks>100:
    print("A+")
elif marks>=89:
    print("A")
elif marks>=79:
    print("B")
elif marks>=69:
    print("C")
elif marks>=59:
    print("D")
else:
    print("Fali")


# Task 2
n = int(input("Enter the number:"))
print("Number for 1 to n:")
for i in range(1,n+1):
    print(i,end="")

print("Number from N to 1:")
for i in range(n, 0, -1):
    print(i, end=" ")

print("Multiplication Tablr:")
for i in range(1,11):
    print(n,"x",i,"=",n*i)


# Task 3
a = float(input("Enter the first number"))
b = float(input("Enter the second number"))
def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
   if b == 0:
    return a/b 

def modulus(a,b):
   if b == 0:
    return a%b

print("Addition",addition (a,b))
print("Subtraction",subtraction (a,b))
print("Multiplication",multiplication (a,b))
print("Division",division (a,b))
print("Modulus",modulus (a,b))


#  Task 4
global_variable = "I am a Global Variable"
def show_variable():
    local_variable = "I am Local Variable"
    print("Local variable:", local_variable)
    print("Global variable:", global_variable)

show_scope()
print("Global variable:", global_variable)


#  Task 5
import math
import random
import datetime

number = 25
square_root = math.sqrt(number)
print("square root of",number,"is:",square_root)

random_number = random.randint(1,100)
print("random number:",random_number)

current_datetime = datetime.datetime.now()
print("current date time:", current_datetime)