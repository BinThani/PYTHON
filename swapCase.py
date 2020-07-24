def swapCase(string):
    result = "" # Initialize variable string.
    for letter in string: # Loop through the string.
        if letter == letter.upper(): # If upper then
            result += letter.lower() # Change to lower.
        else: # Else change it to upper.
            result += letter.upper()
    return result



if __name__ == '__main__':
    print("Enter Anything to swap the Case.")
    userInput = input()
    print(swapCase(userInput))
