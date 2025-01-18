import numpy as np

def accessElements2DArray(arr, rowIndex, colIndex):
    """
    Access an element from a 2D array.
    Checks if the provided rowIndex and colIndex are within bounds of the array.
    """
    # Check bounds using arr.shape
    if (rowIndex < 0 or rowIndex >= arr.shape[0]) or (colIndex <0 or colIndex >= arr.shape[1]):
        print(f"The elment({rowIndex},{colIndex}) is out of bounds")
        return
    else:
        return arr[rowIndex][colIndex]


# Define a 2D Array
# This is a 3x3 identity matrix
# Each diagonal element is 1, and all other elements are 0
twoDimArray = np.array(
   [[1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]]
)

# Print the original 2D Array
# Note: Removed incorrect 'endl' argument and added a blank line for clarity
print(twoDimArray)
print()  # Add an extra blank line before printing the next matrix


"""********** Using insert fucntion **********"""
# Add a new column to the 2D Array
# The new column [[2, 2, 2]] is added at the end (index 3)
newTwoDimArray = np.insert(twoDimArray, 3, [[2, 2, 2]], axis=1)

# Print the updated 2D Array with the new column
print("Colum added at the end using the insert function")
print(newTwoDimArray)
print()  # Add an extra blank line before printing the next matrix

# Add a new row to the 2D Array
# The new column [[1, 1, 1]] is added at the end (index 0)
newTwoDimArray = np.insert(twoDimArray, 0, [[1, 1, 1]], axis=0)

# Print the updated 2D Array with the new row
print("Row added at the start using the insert function")
print(newTwoDimArray)
print()  # Add an extra blank line before printing the next matrix

"""********** Using append function **********"""
# Add a new row to the 2D Array
# The new row [[1, 1, 1]] is added at the end
newTwoDimArray = np.append(twoDimArray, [[1, 1, 1]], axis=0)

# Print the updated 2D Array with the new row
print("Row added at the end using the append function")
print(newTwoDimArray)
print()  # Add an extra blank line before printing the next matrix

# Add another new row to the 2D Array
# The new row [[2, 2, 2]] is added at the end
newTwoDimArray = np.append(twoDimArray, [[2, 2, 2]], axis=0)

# Print the updated 2D Array with the second new row
print("Another row added at the end using the append function")
print(newTwoDimArray)
print()  # Add an extra blank line before printing the next matrix

"""********** Access elements in a 2D Arrays **********"""
while True:
    try:
        row = int(input("Enter row: "))
        col = int(input("Enter Col: "))
        break
    except ValueError as e:
        print(f"Sorry the program encountered an error while reading you input: \nError:\n{e}\nTry again")
    #finally:
        #print("This is just mesage from the finally blocl\n")
        #continue

print(f"The element at ({row},{col}) is: {accessElements2DArray(twoDimArray, row, col)}")
print("")
