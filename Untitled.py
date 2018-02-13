'''
import turtle as t

def right():
    t.left(90)
    t.left(90)
    t.left(90)


def drawStep():
    t.forward(50)
    t.left(90)
    t.forward(50)
    right()

def drawSide():
    drawStep()
    drawStep()
    drawStep()
    t.forward(50)
    t.right(90)

def drawDiamond():
    drawSide()
    drawSide()
    drawSide()
    drawSide()
    
drawDiamond()
'''

# calculator

import math
import random
from math import sqrt

def welcome():
    menu = input('''Welcome to ...Press 1 for basic operations
Press 2 for more advanced math operations
''')
    
    if menu == "1":
        calculate_basic()
    elif menu == "2":
        calculate_adv()

def calculate_basic():
    operation = input('''
Please type the math operation you wnat to complete:
+ for addition
- for subtraction
* for multiplication
% for modulus
/regular division
//integer division
''')
    firstNumber=float(input("Please enter the first number:"))
    secondNumber=float(input("Please enter the second number:"))

if operation == "+":
    print("{}+{}=".format (first Number, secondNumber))
    print(firstNumber+secondNumber)
elif operation == "-":
    print()
    print()
    
else:
    print("You have not typed a valid operator. Run the program again.")
runAgain()

def runAgain():
    again = input('''So you want to calculaate this again? Y/N)
