import numpy as np

# Create a NumPy array of integers
# Use various methods of NumPy arrays to manipulate and display the array.

# 1. Create an array and traverse through its elements
print("1. Create array and traverse:")
my_arr = np.array([1, 2, 3, 4, 5, 6])
for element in my_arr:
    print(f"Element: {element}")
print()

# 2. Access elements via indexes
print("2. Access element by index:")
print(f"Element at index 4: {my_arr[4]}")
print()

# 3. Append a value to the array
print("3. Append value to array:")
my_arr = np.append(my_arr, 7)  # NumPy's append creates a new array
print(f"Array after append: {my_arr}")
print()

# 4. Insert a value at a specific index in the array
"""
For more clarification please look at explinations1.md
"""
print("4. Insert value into the array:")
my_arr = np.insert(my_arr, 0, 22)
print(f"Array after insertion: {my_arr}")
print()

# 5. Extend the array with another array
print("5. Extend array with another array:")
my_arr2 = np.array([10, 11, 12])
my_arr = np.concatenate((my_arr, my_arr2))
print(f"Array after extending: {my_arr}")
print()

# 6. Add items from a list to the array
print("6. Add items from a list to the array:")
my_lst = [111, 222, 333]
my_arr = np.append(my_arr, my_lst)
print(f"Array after adding items from list: {my_arr}")
print()

# 7. Remove a specific element from the array
"""
For more clarification please look at explinations1.md
"""
print("7. Remove an element from the array:")
my_arr = my_arr[my_arr != 111]  # Removes the element 111
print(f"Array after removing 111: {my_arr}")
print()

# 8. Remove the last element from the array
print("8. Remove the last element:")
my_arr = my_arr[:-1]  # Removes the last element
print(f"Array after removing the last element: {my_arr}")
print()

# 9. Fetch the index of a specific element
print("9. Fetch the index of an element:")
print(f"Index of element 22: {np.where(my_arr == 22)[0][0]}")
print()

# 10. Reverse the array
print("10. Reverse the array:")
my_arr = my_arr[::-1]
print(f"Array after reversal: {my_arr}")
print()

# 11. Get buffer information (NumPy equivalent is .nbytes)
print("11. Get buffer information:")
print(f"Total memory (in bytes): {my_arr.nbytes}")
print()

# 12. Check for the number of occurrences of an element
print("12. Count occurrences of an element:")
print(f"Occurrences of 12: {np.count_nonzero(my_arr == 12)}")
print()

# 13. Convert the array to a bytes object
print("13. Convert array to bytes:")
my_arr_toString = my_arr.tobytes()
print(f"Array as bytes: {my_arr_toString}")
print()

# 13.A Convert the bytes back into an array
print("13.A Convert bytes back into an array:")
my_new_arr = np.frombuffer(my_arr_toString, dtype=int)
print(f"New array from bytes: {my_new_arr}")
print()

# 14. Convert array to list
print("14. Convert array to list:")
arr_toList = my_arr.tolist()
print(f"Array as list: {arr_toList}")
print()

# 15. Slice elements of the array
print("15. Slice elements of the array:")
print(f"Full array: {my_arr}")
print(f"First 2 elements (my_arr[:2]): {my_arr[:2]}")
print(f"Elements from index 1 to 3 (my_arr[1:4]): {my_arr[1:4]}")
print(f"Elements from index 2 to the end (my_arr[2:]): {my_arr[2:]}")
print()
