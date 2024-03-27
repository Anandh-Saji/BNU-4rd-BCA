def sequential_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
key = int(input("Enter the number to be searched: "))

result = sequential_search(numbers, key)

if result != -1:
    print(f"Element found at position: {result + 1}")
else:
    print("Element not found in the list.")

input("Press Enter to exit")
