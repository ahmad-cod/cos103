import math


# function to check if an operator is unary (e.g square, sqrt, cube cuberoot) or binary (e.g +, _, *, /)

def is_unary(operator):
  unary_operators = ['square', 'cube', 'sqrt', 'cbrt', '!', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan']
  return operator in unary_operators

def is_binary(operator):
  binary_operators = ['+', '-', '*', '/', '**']
  return operator in binary_operators

def add(x, y):
  return x + y

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
    raise Exception("Math Error!")
  else:
    return a / b

def power(a, b):
  return a ** b

def square(a):
  return a ** 2

def cube(a):
  return a ** 3

def sqrt(a):
  return a ** 0.5

def cbrt(a):
  return a ** (1/3)

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
  
def sin(a):
  return math.sin(a)

def cos(a):
  return math.cos(a)

def tan(a):
  return math.tan(a)

def asin(a):
  return math.asin(a)

def acos(a):
  return math.acos(a)

def atan(a):
  return math.atan(a)