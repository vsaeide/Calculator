import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y:
        return x / y
    else:
        return ZeroDivisionError


def power(x, y):
    return x ** y


def log(x, y):
    if x > 0 and y > 0 and y != 1:
        return math.log(x, y)
    return ValueError


def square(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return ValueError


#############################################################################################3

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Log")
print("7.Square")

##############################################################################################3
while True:

    choice = int(input("\nEnter your choice number: "))

    if choice in range(1, 8):
        if choice in range(1, 7):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == 2:
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == 3:
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == 4:
                result = divide(num1, num2)
                if result == ZeroDivisionError:
                    print("**** Zero Division Error! ****")
                else:
                    print(num1, "/", num2, "=", result)
            elif choice == 5:
                print(num1, "**", num2, "=", power(num1, num2))
            elif choice == 6:
                result = log(num1, num2)
                if result == ValueError:
                    print("Invalid Input")
                else:
                    print("The logarithm of ", num1, " with base ", num2, " is ",result )
        else:
            num = float(input("Enter the number: "))
            if choice == 7:
                result = square(num)

                if result == ValueError:
                    print("Invalid Input")
                else:
                    print("The square of ", num, " is ", result)

        next_calculation = input("Let's do next calculation? (y/n): ")
        if next_calculation == "n":
            break
    else:
        print("Invalid Input")
