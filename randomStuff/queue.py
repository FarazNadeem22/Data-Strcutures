class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.num_nodes = 0
    
    def size(self):
        return self.num_nodes
    
    def enqueue(self, value):
        # Create new_node
        new_node = Node(value=value)

        # Check if queue is empty
        if self.head is None:
            # set the head pointer and the tail pointer to new node 
            self.head = self.tail = new_node
        else:
            # append to the tail of the queue start by making new node point to where self.tail is pointing to 
            new_node.next = self.tail

            # Now set the tail pointer point to new node 
            self.tail.next = new_node
        
        # Increment num_nodes
        self.num_nodes += 1
    
    def dequeue(self):
        # Check if queue is empty
        if self.head is None:
            return None
        else:
            dequeued_node = self.head.value
            self.head = self.head.next
            self.num_nodes -= 1
            return dequeued_node


"""Driver"""

q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')


print("Pass" if (q.size() == 3) else "Fail")
q.enqueue(4)

print("Pass" if (q.size() == 4) else "Fail")

print("Pass" if (q.dequeue() == 'a') else "Fail")

print("Pass" if (q.dequeue() == 'd') else "Fail")


print("Pass" if (q.size() == 2) else "Fail")
