def is_fibonacci(n): 
    a=0
    b=1
    while b < n:
     temp=b
     b=a+b
     a=temp
    return b == n or a == n

n = int(input("Enter a number: "))
if is_fibonacci(n):
    print(n, "belongs to the Fibonacci sequence.")
else:
    print(n, "does not belong to the Fibonacci sequence.")
input(" ")