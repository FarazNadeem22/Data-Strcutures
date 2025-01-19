import numpy as np
from typing import Optional, Tuple

def accessElements2DArray(arr: np.ndarray, rowIndex: int, colIndex: int) -> Optional[int]:
    """
    Access an element from a 2D array.
    Checks if the provided rowIndex and colIndex are within bounds of the array.
    
    Args:
        arr (np.ndarray): The 2D NumPy array.
        rowIndex (int): Row index to access.
        colIndex (int): Column index to access.

    Returns:
        Optional[int]: The accessed element if within bounds, otherwise None.
    """
    try:
        # Ensure rowIndex and colIndex are integers
        rowIndex = int(rowIndex)
        colIndex = int(colIndex)
    except ValueError:
        print("Error: Indices must be integers.")
        return None

    # Check bounds using arr.shape
    if (rowIndex < 0 or rowIndex >= arr.shape[0]) or (colIndex < 0 or colIndex >= arr.shape[1]):
        print(f"The element ({rowIndex},{colIndex}) is out of bounds")
        return None
    else:
        return arr[rowIndex][colIndex]

def traverse2DArray(arr: np.ndarray) -> None:
    """
    Function to traverse a 2D array and print each row with elements separated by commas.
    
    Args:
        arr (np.ndarray): A 2D NumPy array to traverse.

    Returns:
        None
    """
    for i in range(arr.shape[0]):
        # Create a comma-separated string for the current row using join()
        row = ", ".join(str(arr[i][j]) for j in range(arr.shape[1]))
        
        # Print the row with its index
        print(f"Row[{i}]: {row}")

def getInput() -> Tuple[int, int]:
    """
    Get row and column indices from the user.

    Returns:
        Tuple[int, int]: A tuple containing the row and column indices.
    """
    while True:
        try:
            # Prompt the user for row and column indices
            row: int = int(input("Enter row: "))
            col: int = int(input("Enter Col: "))
            return row, col  # Return the indices as a tuple if valid
        except ValueError as e:
            # Handle invalid input errors (e.g., non-integer values)
            print(f"Sorry, the program encountered an error while reading your input: \nError:\n{e}\nTry again")

def search2DArray(arr: np.ndarray, target: int) -> Tuple[Optional[int], Optional[int]]:
    """
    Searches for a target value in a 2D NumPy array.

    Args:
        arr (np.ndarray): The 2D NumPy array to search.
        target (int): The value to search for in the array.

    Returns:
        Tuple[Optional[int], Optional[int]]: The row and column indices of the target if found, otherwise (None, None).
    """
    for i in range(arr.shape[0]):  # Iterate through rows
        for j in range(arr.shape[1]):  # Iterate through columns
            if target == arr[i][j]:  # Check if the target value matches the current element
                return i, j  # Return the indices if the target is found
    return None, None  # Return None, None if the target is not found in the array


    




# Define a 2D Array
# This is a 3x3 identity matrix
# Each diagonal element is 1, and all other elements are 0
twoDimArray: np.ndarray = np.array(
   [[1, 0, 0],
    [0, 1, 0],
    [0, 22, 1]]
)

# Print the original 2D Array
print("Original 2D Array:")
print(twoDimArray)
print()  # Add an extra blank line before printing the next matrix


"""********** Using insert function **********"""
# Add a new column to the 2D Array
# The new column [[2, 2, 2]] is added at the end (index 3)
newTwoDimArray: np.ndarray = np.insert(twoDimArray, 3, [[2, 2, 2]], axis=1)

# Print the updated 2D Array with the new column
print("Column added at the end using the insert function:")
print(newTwoDimArray)
print()  # Add an extra blank line before printing the next matrix

# Add a new row to the 2D Array
# The new row [[1, 1, 1]] is added at the start (index 0)
newTwoDimArray = np.insert(twoDimArray, 0, [[1, 1, 1]], axis=0)

# Print the updated 2D Array with the new row
print("Row added at the start using the insert function:")
print(newTwoDimArray)
print()  # Add an extra blank line before printing the next matrix

"""********** Using append function **********"""
# Add a new row to the 2D Array
# The new row [[1, 1, 1]] is added at the end
newTwoDimArray = np.append(twoDimArray, [[1, 1, 1]], axis=0)

# Print the updated 2D Array with the new row
print("Row added at the end using the append function:")
print(newTwoDimArray)
print()  # Add an extra blank line before printing the next matrix

# Add another new row to the 2D Array
# The new row [[2, 2, 2]] is added at the end
newTwoDimArray = np.append(twoDimArray, [[2, 2, 2]], axis=0)

# Print the updated 2D Array with the second new row
print("Another row added at the end using the append function:")
print(newTwoDimArray)
print()  # Add an extra blank line before printing the next matrix

"""********** Access elements in a 2D Arrays **********"""

# Print the 2D Array to provide context to the user
print("Current 2D Array:")
print(twoDimArray)
print()  # Add an extra blank line for readability

# Get row and column indices from the user
row, col = getInput()

# Access and print the specified element
result = accessElements2DArray(twoDimArray, row, col)

# Check if result is not None 
if result is not None:
    print(f"The element at ({row},{col}) is: {result}\n")
else:
    print("")

"""********** Traversal - 2D Array **********"""
# Print the 2D Array to provide context to the user
print("Traversing: Current 2D Array:")
print(twoDimArray)
print()  # Add an extra blank line for readability
traverse2DArray(twoDimArray)


"""********** Search 2D Array **********"""
target = 22
row, col = search2DArray(twoDimArray, target)
if row is not None:
    print(f"Target {target} found location ({row}, {col})")
else:
    print("Target not found")