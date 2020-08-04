# Recursion
"""
Base Case: Condition used in recursion to exit out of the function
Recursive Case: Function calling itself n Times until it achieves the base Case

Difference Between Iteration and Recursion:
The way they end.
Itteration Will end when it reaches the sequence
Recursion Will end when it achieves the base Case.

Cons With Recursion:
High memory.
"""

def factorial(n):
    if n == 0:  # Base Case
        return 1
    else:
        return n*factorial(n-1)  # Recursive Case

if __name__ == '__main__':
    print(factorial(4))
