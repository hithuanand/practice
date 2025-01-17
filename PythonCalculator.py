#Python Calculator
from arithematicExercises2 import result

operator = input("Enter the operator (+ - / *)")

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

if operator == "+":
    result = num1+num2
    print(result)
elif operator == "-":
    result = num1-num2
    print(result)
elif operator == "/":
    result = num1/num2
    print(result)
elif operator == "*":
    result = num1*num2
    print (result)

