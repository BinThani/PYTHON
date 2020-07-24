myPets = ["Sango", "Chango"] # List of the pets.
print("Enter a pet name: ")
name = input()

if name not in myPets: # If the name of the pet is not in the list then do V.
    print("I do not have a pet name" + name)
else: 
    print(name + " Is my pet")
