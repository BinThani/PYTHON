# Dictionary
"""
Keys are commonly strings or numbers
Initilization V
Dictionary KEY:VALUE
"""
def dictionary():
    # Initialization
    # Example 1
    cars = {"Car": "Mustang",
            "Model": 1996}

    print("Car name " + cars["Car"])
    print("Model: " + str(cars["Model"]))

    # Add an entry
    cars["Month"] = "January"
    print("Month: " + cars["Month"])

    print("\nExample #2\n")
    # Example 2
    Grades = {"Ana": "B+",
              "Mohammed": "B",
              "John": "F+"}

    print("Ana Grades: " + Grades["Ana"])
    print("Mohammed Grades: " + Grades["Mohammed"])
    print("John's Grades: " + Grades["John"])

    # Overwrite Grades
    Grades["Mohammed"] = "D"
    print("New Grades Mohammed: " + Grades["Mohammed"])

    # Iterate Instead of printing
    print("\nIteration Of Grades\n")
    for key, value in Grades.items():
        print(key + " " + value)

    # Test if key in dictionary
    print("\nTest of key in Dictionary\n")
    print("John" in Grades)  # --> True John is in dictionary
    print("Daniel" in Grades)# --> False Daniel Is not in dictionary.

    # Delete an Entry
    print("\nDeleting An Entry\n")
    del(Grades["John"])  # --> Removes john out of the dict

    print("New Dictionary")
    for key, value in Grades.items():
        print("Key: " + key + " Grades: " + value)

    # Get keys/Values
    print("\nKeys and Values\n")
    print(Grades.keys())
    print(Grades.values())

if __name__ == '__main__':
    dictionary()


