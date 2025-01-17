## NumPy Array Operations Explained

### **Removing a Specific Element from a NumPy Array**

```python
# 7. Remove a specific element from the array
print("7. Remove an element from the array:")

# Use logical indexing to exclude the element `111`
# Explanation:
# - `my_arr != 111` creates a Boolean array where each element is `True` if it is not equal to 111 and `False` otherwise.
# - Indexing `my_arr[my_arr != 111]` returns only the elements for which the condition is `True`.
# - This effectively removes the value 111 from the array.

my_arr = my_arr[my_arr != 111]  # Removes the element 111

# Display the array after removing the element
print(f"Array after removing 111: {my_arr}")
print()
```

#### **Detailed Steps**:
1. **Condition Creation**:
   - `my_arr != 111` creates a condition (`Boolean array`) where each element of `my_arr` is compared to `111`. 
     Example:
     ```python
     my_arr = np.array([1, 2, 3, 111, 4])
     my_arr != 111  # Output: [True, True, True, False, True]
     ```

2. **Logical Indexing**:
   - Applying this condition as an index (`my_arr[condition]`) selects only elements where the condition is `True`.
     Example:
     ```python
     my_arr[my_arr != 111]  # Output: [1, 2, 3, 4]
     ```

3. **Update the Array**:
   - Assign the resulting array back to `my_arr` to permanently remove the element.

#### **Example Output**:
Input:
```python
my_arr = np.array([1, 2, 3, 111, 4])
my_arr = my_arr[my_arr != 111]
```
Output:
```
Array after removing 111: [  1   2   3   4]
```

---

### **Inserting a Value at a Specific Index in a NumPy Array**

```python
# 4. Insert a value at a specific index in the array
print("4. Insert value into the array:")

# Use NumPy's `insert()` method to insert a value
# Explanation:
# - `np.insert(array, index, value)` takes three arguments:
#   1. `array`: The original array where the value will be inserted.
#   2. `index`: The position at which the value should be inserted.
#   3. `value`: The value to be inserted.
# - This creates a new array with the specified value inserted at the given index, shifting all subsequent elements to the right.

my_arr = np.insert(my_arr, 0, 22)  # Insert 22 at the beginning (index 0)

# Display the array after insertion
print(f"Array after insertion: {my_arr}")
print()
```

#### **Detailed Steps**:
1. **`np.insert()` Function**:
   - `np.insert(array, index, value)`:
     - `array`: The original NumPy array.
     - `index`: Position where the new value is inserted. If `index=0`, the value is added at the start.
     - `value`: The actual value to be inserted.

2. **Shift and Create a New Array**:
   - The function does not modify the original array but creates a new array with the inserted value.
   - Example:
     ```python
     my_arr = np.array([1, 2, 3])
     np.insert(my_arr, 0, 22)  # Output: [22, 1, 2, 3]
     ```

3. **Update the Array**:
   - Assign the newly created array back to `my_arr` to reflect the change.

#### **Example Output**:
Input:
```python
my_arr = np.array([1, 2, 3])
my_arr = np.insert(my_arr, 0, 22)
```
Output:
```
Array after insertion: [22  1  2  3]
