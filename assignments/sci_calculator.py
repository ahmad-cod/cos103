import math
from operations import *

def calculator():
  print('Welcome to Aroyehun mini scientific calculator...')
  print('Supported operators: +, -, *, /, **')
  print('To exit, type "exit".')

  x = float(input("Enter a number: "))
  operator = input("Enter an operator: ")
  if is_binary(operator):
    y = float(input("Enter another number: "))
    
    match operator:
      case '+':
        print(add(x, y))

      case '-':
        print(subtract(x, y))

      case '*':
        print(multiply(x, y))

      case '/':
        print(divide(x, y))

      case '**':
        print(power(x, y))

      case _:
        raise Exception("Syntax Error!")


  elif is_unary(operator):
    match operator:
      case 'square':
        print(square(x))

      case 'cube':
        print(cube(x))

      case 'sqrt':
        print(sqrt(x))
      
      case 'cbrt':
        print(cbrt(x))

      case '!':
        print(factorial(x))

      case '_':
        raise Exception("Syntax Error!")
      
  else:
    raise Exception("Syntax Error!")
  
calculator()

while True:
  user_choice = input("Do you want to perform another calculation? (yes/no): ")
  if user_choice.lower() == 'yes' or user_choice.lower() == 'y':
    calculator()
  elif user_choice.lower() == 'no' or user_choice.lower() == 'n' :
    print("Thank you for using Aroyehun's calculator!")
    break
  else:
    print("Invalid choice. Please enter 'yes' or 'no'.")




















# User Flow:
# Ask User to input a number,
# User inputs an operator
# Using the is_binary function from the operations module, check if the type of operator is binary
# if operator is binary, then request for another number, else if it's unary, print the result
# return a syntax error, if a user doesn't input a valid value where he's expected to input a value
# 
# after a calculation is done prompt the user, if he wants to perform another calculation
# Let there be a welcome and introduction guide to how to use the calculator

    # if operator == '+':
    #   print(add(x, y))
    # elif operator == '-':
    #   print(subtract(x, y))
    # elif operator == '*':
    #   print(multiply(x, y))
    # elif operator == '/':
    #   print(divide(x, y))
    # elif operator == '**':
    #   print(power(x, y))

    # if operator == 'square':
    #   print(square(x))
    # elif operator == 'cube':
    #   print(cube(x))
    # elif operator == 'sqrt':
    #   print(sqrt(x))
    # elif operator == 'cbrt':
    #   print(cbrt(x))
    # elif operator == '!':
    #   print(factorial(x))
    # elif operator == 'sin':
    #   print(sin(x))
    # elif operator == 'cos':
    #   print(cos(x))
    # elif operator == 'tan':
    #   print(tan(x))
    # elif operator == 'asin':
    #   print(asin(x))
    # elif operator == 'acos':
    #   print(acos(x))
    # elif operator == 'atan':
    #   print(atan(x))