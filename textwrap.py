import textwrap

# Wraps user text based on widthInput
# If userInp was HELLO WORLD
# and width was 5
# Output would be:
# HELLO 
# WORLD

# Function
def wrap(string, maxwidth):
    string = textwrap.fill(string, maxwidth)
    return string

# Userinput
userInput = str(input())
widthInput = int(input())

# Result
print(wrap(userInput, widthInput))
