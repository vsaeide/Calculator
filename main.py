def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


print("Select operation.")
print("1.Add")
print("2.Subtract")

while True:

    choice = int(input("\nEnter your choice number: "))

    if choice in range(1, 3):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 2:
            print(num1, "-", num2, "=", subtract(num1, num2))

        next_calculation = input("Let's do next calculation? (y/n): ")
        if next_calculation == "n":
            break
    else:
        print("Invalid Input")
