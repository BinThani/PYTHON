def list():
    # Initialize a list
    ar = [5, 4, 2, 3]

    # Original list
    print("Original List", ar)

    # Add an element to the an to the end of the list
    ar.append(10)
    ar.append(1)
    print("appended array: ", ar)

    # Remove the last element
    ar.pop()
    print("Popped last item: ", ar)

    # Remove element at specified location
    ar.remove(10)
    print("Removed at specified location", ar)

    # Accessing elements using splice
    print("print all element", ar[:])
    print("last two elements", ar[2:])
    print("First two elements ignore last", ar[0:2])
    print("Every two elemnts print", ar[::3])

    # Acess item using index Number
    print("Where item 5 is located at:", ar.index(5))

    # Loop the list
    print("\n")
    print("Loop the array using enumerate() to print both Index + Item")
    for index, item in enumerate(ar):
        print("Number at index", str(index), " Number : ", str(item))
    print("\n")

    # Reverse the array
    ar.reverse()
    print("Reversed array: ", ar)

    # Sort the array
    ar.sort()
    print("Sorted array: ", ar)



def main():
    list()

if __name__ == '__main__':
    main()


