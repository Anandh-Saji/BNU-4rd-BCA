## [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Lemon+milk&color=F7000&lines=THIS+IS+A+GITHUB+REPOSITORY;Created+by+Anandh)](https://git.io/typing-svg)

   <br> 
</p>

## PROGRAM 1 
## (CECK IF A NUMBER BELONGS TO FIBONACCI SEQUENCE)

```
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
```

## PROGRAM 2 
## (SOLVE QUADRATIC EQUATION.)

```
import math
def solve_quadratic(a,b,c):
    discriminant=b**2-4*a*c
    if discriminant >= 0:
        root1=(-b+ mth.sqrl(discriminant))
        root2=(-b -math.sqrl(discriminant))
        return(root1,root2)
    else:
        return None
a = float(input("Enter the coefficients for X^2(a): "))
b = float(input("Enter the coefficients for x(b): "))
c = float(input("Enter the constant (c): "))

roots = solve_quadratic(a,b,c)

if roots is not None:
    print(f"The root of the equation {a}x^2+{b}x+{c}=0 are {roots[0]:.2f} and {root[1]:.2f}")
else:
    print("the given equation has no real roots") 
input(" ")
```
## PROGRAM 3
## (FIND THE SUM OF N NATURAL NUMBERS)

```
n = int(input("Enter a natural number: "))
sum_of_n_numbers = n * (n+1) // 2
print(f"The sub of the first {n} natural numbers is: {sum_of_n_numbers}")
input(" ")
```
## PROGRAM 4
## (DISPLAY MULTIPLICATION TABLE)

```
num = int(input("enter the number: "))
for i in range(1,11):
   print (f"{num} x {i} = {num*i}")
input(" ")
```
## PROGRAM 5
## (CHECK ID GIVEN NUMBER IS PRIME OR NOT)

```
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
```
