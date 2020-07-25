"""
List Comprehension
Some Ideas to keep in Mind.
he common ways to describe lists are:
S = {x² : x in {0 ... 9}}
V = (1, 2, 4, 8, ..., 2¹²)
M = {x | x in S and x even}

S is a sequence that contains values between 0 and 9 included
and each value is raised to the power of two.

The sequence V, on the other hand,
contains the value 2 that is raised to a certain power x.
The power x starts from 0 and goes till 12.

Lastly, the sequence M contains only the even elements from the sequence S.
"""

S = [x**2 for x in range(10)] # Power of 2.
V = [2**i for i in range(13)] # 2 Raised to a power.
print(f"{S}\n{V}")
M = [x for x in S if x % 2 == 0]
print(M)

"""
Question
list_variable = [x for x in iterable] Now it's your turn to go ahead and get started with list comprehensions in Python! 
Let's stick close to the mathematical lists that you have seen before: Q = {x3: x in {0 ... 10}} 
Try to code the above line of code in your python shell and the output should look like: 
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""


# Practice/Answer.
Q = [x**3 for x in range(11)]
print(Q)

# Practice 2
numbers = range(10)  # Numbers from 0 to 9 (0 1 2 ... 9)

# Initialize "new_list"    # Line 41 through 50 is the opposite of a list comprehension
new_list = []

# Add values to "new_list"
for n in numbers:
    if n % 2 == 0:  # Check if the element is even.
        new_list.append(n**2)  # Raise the element to the power of 2 and append it to the list.

# Print "new_list"
print(new_list)

# List comprehension of the above ^. in 2 Lines of code...
notnew_list = [n**2 for n in numbers if n % 2 == 0]
print(notnew_list)

# TBContinued.
# Source https://www.datacamp.com/community/tutorials/python-list-comprehension


