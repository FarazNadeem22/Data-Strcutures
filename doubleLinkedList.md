# Double Linked List

This Python code demonstrates the implementation of a doubly linked list.

## Program Overview

This program consists of two classes:
- `Node`: Defines a node in the doubly linked list.
- `doubleLinkList`: Implements various operations on the doubly linked list.

## Classes

### `Node` Class

- **Attributes**:
  - `data`: Stores the data for a node.
  - `next`: Points to the next node.
  - `prev`: Points to the previous node.

### `doubleLinkList` Class

- **Attributes**:
  - `head`: Points to the head node of the list.

### Methods

#### `print(forward=True)`

- **Functionality**: Prints the doubly linked list either forward or backward.
- **Arguments**:
  - `forward` (bool, optional): Determines the printing direction (default is forward).
  
#### `prettyPrint(forward=True)`

- **Functionality**: Enhanced print of the doubly linked list in either direction.
- **Arguments**:
  - `forward` (bool, optional): Determines the printing direction (default is forward).

#### `insert_empty(data)`

- **Functionality**: Inserts a node into an empty list.
- **Arguments**:
  - `data`: Value for the node to be inserted.

#### `insert_start(data)`

- **Functionality**: Inserts a node at the start of the list.
- **Arguments**:
  - `data`: Value for the node to be inserted.

#### `insert_end(data)`

- **Functionality**: Inserts a node at the end of the list.
- **Arguments**:
  - `data`: Value for the node to be inserted.

#### `insert_list_end(lst)`

- **Functionality**: Inserts elements of a list as nodes at the end of the list.
- **Arguments**:
  - `lst`: List containing values to be inserted as nodes.

#### `insert_after(data, target)`

- **Functionality**: Inserts a node after a specified target node.
- **Arguments**:
  - `data`: Value for the node to be inserted.
  - `target`: Value of the target node.

#### `insert_before(data, target)`

- **Functionality**: Inserts a node before a specified target node.
- **Arguments**:
  - `data`: Value for the node to be inserted.
  - `target`: Value of the target node.

#### `delete_before(target)`

- **Functionality**: Deletes the node before the specified target node.
- **Arguments**:
  - `target`: Value of the target node.

#### `delete_after(target)`

- **Functionality**: Deletes the node after the specified target node.
- **Arguments**:
  - `target`: Value of the target node.

#### `delete_node(ptr)`

- **Functionality**: Deletes a specified node.
- **Arguments**:
  - `ptr`: Pointer to the node to be deleted.

#### `delete_target(target)`

- **Functionality**: Deletes a specified target node.
- **Arguments**:
  - `target`: Value of the target node.
