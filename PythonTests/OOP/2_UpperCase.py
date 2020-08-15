# OOP

class Upperstring(object):
    def __init__(self, inputstring):
        self.inputstring = inputstring

    def upperCase(self):
        return self.inputstring.upper()

if __name__ == '__main__':
    # Ask for input to Upper
    userInput = str(input("Write a sentence that you want to convert into uppercase: "))

    # Variables
    upper = Upperstring(userInput)

    # Output
    print(upper.upperCase())
