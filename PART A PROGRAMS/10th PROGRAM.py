
stack = []

while True:
    print("\n1: Push")
    print("2: Pop")
    print("3: Peek")
    print("4: Display stack")
    print("5: Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter the number to be pushed: "))
        stack.append(num)

    elif choice == 2:
        if len(stack) < 1:
            print("Stack is empty. Nothing to pop.")
        else:
            print("Popped value: ", stack.pop())

    elif choice == 3:
        if len(stack) < 1:
            print("Stack is empty.")
        else:
            print("Topmost value: ", stack[-1])

    elif choice == 4:
        print("Stack: ", stack)

    elif choice == 5:
        break

    else:
        print("Invalid choice. Please choose again.")
