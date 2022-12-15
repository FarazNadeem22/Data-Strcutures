class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self) -> None:
        self.head = None
        self.num_nodes = 0
    
    def push(self, value):
        # create new node 
        new_node = Node(value)

        # Check case for empty stack
        if self.head is None:
            # Self itself to the head pointer 
            self.head = new_node
        else:       
            # Set the new point pointer next to the current head 
            new_node.next = self.head

            # Set the head pointer to point to new node
            self.head = new_node
 
        # Increment the new node count
            self.num_nodes += 1

    def pop(self):
        # Check is stack is empty
        if self.head is None:
            return None
        else:
            pop_node = self.head.value
            self.head = self.head.next
            self.num_nodes -= 1
            return pop_node

    def Print_Stack(self):
        ptr = self.head
        while ptr.next is not None:
            print(f"Value: {ptr.value}")
            ptr = ptr.next
        print(f"Value: {ptr.value}")


"""Driver"""
# stack = Stack()

# stack.push('1')
# stack.push('2')
# stack.push('3')

# stack.pop()
# stack.pop()       

# stack.push(4)
# stack.push(5)

# stack.pop()

# stack.push(6)

# stack.Print_Stack()
