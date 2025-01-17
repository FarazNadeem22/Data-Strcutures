# Python Linked List Implementation

This Python program provides a basic implementation of a singly linked list with various operations such as insertion, deletion, and printing.

## Classes

### `Node`

Represents a node in the linked list.

- **Attributes**:
  - `val`: Value/data stored in the node.
  - `next`: Reference to the next node in the list.

### `LinkedList`

Represents a singly linked list.

- **Attributes**:
  - `head`: Reference to the first node in the list.

- **Methods**:
  - `insert_begin(data)`: Inserts a new node at the beginning of the linked list.
  - `insert_end(data)`: Inserts a new node at the end of the linked list.
  - `insert_list(lst, reverse=False)`: Creates a linked list from a list, with an option to reverse the order of insertion.
  - `insert_after_node(data, value)`: Inserts a node after a given node with a specific value.
  - `insert_before_node(data, value)`: Inserts a node before a given node with a specific value.
  - `delete_node(value)`: Deletes a node with a specific value from the linked list.
  - `printLinkedList()`: Prints the elements of the linked list.
  - `prettyPrint()`: Prints the elements of the linked list in a more readable format.

