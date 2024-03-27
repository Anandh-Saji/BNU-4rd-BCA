# Get user input for a string
str = input("Enter a string: ")

print("Capitalized string: ", str.capitalize())

print("String in uppercase: ", str.upper())

print("String in lowercase: ", str.lower())

print("Is string alphanumeric: ", str.isalnum())

print("Is string numeric: ", str.isnumeric())

substring = input("Enter a substring to find in the user string: ")
print(f"Substring '{substring}' found at index: ", str.find(substring))

old_substring = input("Enter the substring to replace: ")
new_substring = input("Enter the new substring: ")
print("Replaced string: ", str.replace(old_substring, new_substring))

print("List of words: ", str.split())
