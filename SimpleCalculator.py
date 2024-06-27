import random
import math
def add(x,y):
        return x + y
def sub(x,y):
        return x - y
def multi(x,y):
        return x * y
def div(x,y):
        return x/y
def square(x,y):
        return x ** y 
def sqrt(x,y):
        return x ** (1/y)
def mod(x,y):
        return x % y
def mod(x,y):
        return x // y
print("Select operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square")
print("6. Squareroot")
print("7. Modulus")
while True:
  choice = input("Enter choice(1/2/3/4/5/6/7): ")
  if choice in ('1','2','3','4','5','6','7'):
          try:
            num1 = float(input("Enter the number: "))
            num2 = float(input("Enter the number: "))
          except ValueError: 
                  print("Invalid Input")
                  continue
          if choice == '1':
                  print(num1, "+", num2, "=", add(num1, num2))
          elif choice == '2':
                  print(num1, "-", num2, "=", sub(num1, num2))
          elif choice == '3':
                  print(num1, "*", num2, "=", multi(num1, num2))
          elif choice == '4':
                  print(num1, "/", num2, "=", div(num1, num2))
          elif choice == '5':
                  print(num1, "^", num2, "=", square(num1, num2))
          elif choice == '6':
                  print(num1, "sqrt", num2, "=", sqrt(num1, num2))
          elif choice == '7':
                  print(num1, "%", num2, "=", mod(num1, num2))
          next_cal = input("Next Calculation??: ")
          if next_cal == 'no':
                  break
  else:
    print("Invalid")

                        