def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("\nThe result is: ", add(num1, num2))
elif choice == '2':
    print("\nThe result is: ", subtract(num1, num2))
elif choice == '3':
    print("\nThe result is: ", multiply(num1, num2))
elif choice == '4':
    print("\nThe result is: ", divide(num1, num2))
else:
    print("\nInvalid Input!")
