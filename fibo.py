"""Write a program non-recursive and recursive program to calculate Fibonacci numbers and
analyze their time and space complexity."""

n = int(input("Enter the number of fibonacci numbers to be generated:"))

##Iterative (Non_recursive) Fibonacci Program
def fibonacci_iterative(n):
    if n<=1:
        return n
    a,b = 0,1
    for _ in range (2, n+1):
        a,b = b, a+b
    return b

#n = 10
print(f"Iterative fibonacci of {n} is {fibonacci_iterative(n)}")


#Recursive Fibonacci Program
def fibonacci_recursive(n):
    if n<=1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

#n = 10
print(f"Recursive fibonacci of {n} is {fibonacci_recursive(n)}")


#Optimized Recursive Approach (using memorization)
def fibonacci_memorized(n, memo={}):
    if n<=1:
        return n
    if n not in memo:
        memo[n] = fibonacci_memorized(n-1, memo) + fibonacci_memorized(n-2, memo)
    return memo[n]

#n = 10
print(f"Memorized Recursive Fibonacci of {n} is {fibonacci_memorized(n)}")