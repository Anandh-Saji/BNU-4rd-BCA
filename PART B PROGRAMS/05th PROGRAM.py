def is_prime(num):
    if num <= 1:
       return False
    for i in range(2, num):
        if num % i == 0:
          return False
    return True 

n = int(input("Enter a number: "))
if is_prime(n):
   print(f"{n} is a prime number")
else:
     print(f"{n} is not a prime number")
input(" ") 