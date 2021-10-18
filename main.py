

def add(x, y):
    return x + y


print("Select operation.")
print("1.Add")



while True:

    choice = int(input("\nEnter your choice number: "))

    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print(num1, "+", num2, "=", add(num1, num2))

        next_calculation = input("Let's do next calculation? (y/n): ")
        if next_calculation == "n":
            break
    else:
        print("Invalid Input")