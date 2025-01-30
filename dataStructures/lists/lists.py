# Lists 
from typing import Any

def printList(lst: list) -> None:
    """
    Function to traverse through the list and print elements as a comma-separated string.
    Ensures all items are converted to strings before joining.
    """
    lst_ = ", ".join(str(items) for items in lst)  # Convert items to string and join with commas
    print(lst_)  # Print formatted list
    print("")    # Print an extra blank line for readability

def searchTarget(lst: list, target: Any) -> bool:
    if target in lst:
        print(f"{target}, found in list")
        return 1
    else:
        print(f"{target}, not found in list")
        return 0

# Create a shopping list with string elements
shopping_list = ["Meat", "Milk", "Flour", "Sugar"]
print("Original shopping list:")
print(shopping_list)
print("")

# Traversing through the shopping list
print("Printing shopping list using function:")
printList(shopping_list)

# Accessing an element in the shopping list
print("Accessing third item in the list:")
print("Item:", shopping_list[2])
print("")

# Updating an element in the list
print("Updating second item (Milk -> Bread):")
shopping_list[1] = "Bread"
printList(shopping_list)

"""********** Insert, Append, and Extend **********"""

# Creating a new list of integers
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Initial integer list:")
printList(my_list)
print("")

# Insert an element at the beginning of the list
print("Inserting 22 at index 0:")
my_list.insert(0, 22)
printList(my_list)

# Append a new element to the end of the list
print("Appending 'f' to the list:")
my_list.append("f")
printList(my_list)

# Extend the list by adding another list of elements
print("Extending the list with [22, 33, 44, 55]:")
new_list = [22, 33, 44, 55]
my_list.extend(new_list)
printList(my_list)

"""********** Slicing a List **********"""

# Slicing the first two elements
print("Slicing first two elements:")
printList(my_list[:2])

# Replacing the first two elements with new values
print("Replacing first two elements with 'x' and 'y':")
my_list[:2] = ['x', 'y']
printList(my_list)

# Removing the first element using pop
print("Removing the first element using pop():")
my_list.pop(0)
printList(my_list)

# Popping and printing the last element
print("Popping the last element:")
print(my_list.pop())
print("")

# Deleting an element at index 10
print("Deleting element at index 10:")
del my_list[10]
printList(my_list)

# Removing an element by value
print("Removing 'y' from the list:")
my_list.remove('y')
printList(my_list)


"""********** Searching for an element in a list **********"""


       