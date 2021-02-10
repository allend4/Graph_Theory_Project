"""verifying the collatz conjecture."""

# David Allen

def f(n):
    # If n is even
    if n % 2 == 0:
        return n / 2
    #If n is odd
    elif n % 2 == 1:
        return (3 * n) + 1
    else:
        return None

def collatz(n):
    # loop unitl n is 1
    while n != 1:
        n = f(n)
        return True

print(collatz(10))
print(collatz())

