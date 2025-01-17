from array import *

# Create an array of integers
# Use various methods of the array module to manipulate and display the array.

# 1. Create an array and traverse through its elements
print("1. Create array and traverse:")
my_arr = array('i', [1, 2, 3, 4, 5, 6])
for element in my_arr:
    print(f"Element: {element}")
print()

# 2. Access elements via indexes
print("2. Access element by index:")
print(f"Element at index 4: {my_arr[4]}")
print()

# 3. Append a value to the array
print("3. Append value to array:")
my_arr.append(7)
print(f"Array after append: {my_arr}")
print()

# 4. Insert a value at a specific index in the array
print("4. Insert value into the array:")
my_arr.insert(0, 22)
print(f"Array after insertion: {my_arr}")
print()

# 5. Extend the array with another array
print("5. Extend array with another array:")
my_arr2 = array('i', [10, 11, 12])
my_arr.extend(my_arr2)
print(f"Array after extending: {my_arr}")
print()

# 6. Add items from a list to the array using fromlist() method
print("6. Add items from a list using fromlist():")
my_lst = [111, 222, 333]
my_arr.fromlist(my_lst)
print(f"Array after adding items from list: {my_arr}")
print()

# 7. Remove a specific element from the array
print("7. Remove an element from the array:")
my_arr.remove(111)
print(f"Array after removing 111: {my_arr}")
print()

# 8. Remove the last element from the array using pop()
print("8. Remove the last element using pop():")
my_arr.pop()
print(f"Array after popping the last element: {my_arr}")
print()

# 9. Fetch the index of a specific element
print("9. Fetch the index of an element:")
print(f"Index of element 22: {my_arr.index(22)}")
print()

# 10. Reverse the array
print("10. Reverse the array:")
my_arr.reverse()
print(f"Array after reversal: {my_arr}")
print()

# 11. Get buffer information
print("11. Get buffer information:")
print(f"Buffer info: {my_arr.buffer_info()}")
print()

# 12. Check for the number of occurrences of an element
print("12. Count occurrences of an element:")
print(f"Occurrences of 12: {my_arr.count(12)}")
print()

# 13. Convert the array to a bytes object
print("13. Convert array to bytes (tobytes()):")
my_arr_toString = my_arr.tobytes()
print(f"Array as bytes: {my_arr_toString}")
print()

# 13.A Convert the bytes back into an array
print("13.A Convert bytes back into an array:")
my_new_arr = array('i')
my_new_arr.frombytes(my_arr_toString)
print(f"New array from bytes: {my_new_arr}")
print()
 
# 14. Convert array to list
print("14. Convert array to list:")
arr_toList = my_arr.tolist()
print(f"Array as list: {arr_toList}")
print()

# 15. Slice elements of the array
print("15. Slice elements of the array:")
# Demonstrate slicing operations on the array
print(f'Full array: {my_arr}')
print(f"First 2 elements (my_arr[:2]): {my_arr[:2]}")
print(f"Elements from index 1 to 3 (my_arr[1:4]): {my_arr[1:4]}")
print(f"Elements from index 2 to the end (my_arr[2:]): {my_arr[2:]}")
print()
