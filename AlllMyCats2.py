catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + # Everytime it loops increases by 1 and so on.
          ' (Or enter nothing to stop.):')
    name = input()
    if name == "":
        break
    catNames = catNames + [name] # List Concatenation

# Names.
print("The cat names are:")
for name in catNames:
    print("" + name)
