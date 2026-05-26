# recursive function to find the nth fibnoacci number 
def fibnoacci(n:int)->int:
    if(n==0):
        return 0
    elif(n==1):
        return 1    
    else:return fibnoacci(n-1)+fibnoacci(n-2)
print(fibnoacci(4))

# ---------------------------------------------------------------


# using memoization to optimize the recursive function
def fibnoacci1_genrator(n:int):
    a, b = 0, 1 
    for _ in range(n):
        yield a
        a, b = b, a + b 

print(list(fibnoacci1_genrator(10)))

# ---------------------------------------------------------------
# factorial of a number using recursion
def factorial(n:int)->int:
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))