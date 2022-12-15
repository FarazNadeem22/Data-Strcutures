import sys 

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_begin(self,data):
        """inserts a new node at the start of the linked list 
           https://www.youtube.com/watch?v=B-zO18TJKYQ
        Args:
            data (number): data part of the node  stored at self.val
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_end(self,data):
        """inserts a new node at the end of the linked list 

        Args:
            data (number): data part of the node stored at self.val
        """
        #Create new node
        new_node = Node(data)
        #Check if list is empty
        if self.head == None:
            #empty list
            self.head = new_node
        else:
            #Now go to the end of the linked list the "LAST NODE"
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            #now place new_node at the end 
            ptr.next = new_node    
            #new_node.next = None
            
    def insert_list(self, lst, reverse = False):
        """Takes a lst and makes a linked list out of it. 

        Args:
            lst (list): list of elements
            reverse (bool, optional): Optional reverse order, defalut insert at the start of list 
        """
        if reverse:
            for element in lst:
                self.insert_end(element)
        else:
            for element in lst:
                self.insert_begin(element)
    
    def insert_after_node(self,data, value):
        """inserts a node in a linked list after a given node 

        Args:
            data (any elements): the element you need to add to the list 
            value (element in the list): The value to find in the list after which we wil insert the given data
        """
        try:
            #Create new node 
            new_node = Node(data)
            #find position 
            ptr = self.head
            #find target position
            while ptr.val != value:
                ptr = ptr.next
            #inset after this node 
            tmp = ptr.next
            ptr.next = new_node
            new_node.next = tmp
        except:
            print("{} not found in the linked list".format(value))
        
    def insert_before_node(self,data,value):
        """inserts a node in a linked list before a given node 
        
        Args:
            data (Any element):the element you need to add to the list 
            value (target element in the list): The value to find in the list before which we wil insert the given data
        """
        try:
            #Create new node 
            new_node = Node(data)
            #find position 
            ptr = self.head
            #find target position
            while ptr.next.val != value:
                ptr = ptr.next
            #inset after this node 
            tmp = ptr.next
            ptr.next = new_node
            new_node.next = tmp
        except:
            print("{} not found in the linked list".format(value))
        
    def remove(self, data):
        pass
    
    def printLinkedList(self):
        #check if LL empty 
        if self.head is None:
            #if empty print 
            print("Linked List is Empty")
        else:
            #if not empty then go through each node
            ptr = self.head
            while ptr is not None:
                print(ptr.val)
                ptr = ptr.next
      
    def delete_node(self,value):
        """Deletes a node from a linked list 
        Args:
            value (element in the list): Target element in the list to delete 
        """
        try:
            #set Ptr to head ptr
            ptr = self.head
            if ptr.val == value:
                self.head = ptr.next
                return
            #Stop ptr at postion before target node
            while ptr.next.val != value:
                ptr = ptr.next
            #set a temprorary pointer to node before the target node 
            tmp = ptr
            #Move pointer forward by 1 
            ptr = ptr.next
            #Set tmp pointer to the element the target node is pointing to 
            tmp.next = ptr.next
        except:
            print("{} not found in list".format(value))
                        
    def prettyPrint(self):
        ptr = self.head   
        while ptr and ptr.next:
            sys.stdout.write(str(ptr.val)+"->")
            ptr = ptr.next       
        if ptr:
            print(ptr.val)
        else:
            print("Empty List")
        
         
# LL = LinkedList()
lst = [1,2,3,4,5,6,7,8,9,10]
# LL.insert_list(lst)
# LL.prettyPrint()
# LL.insert_end(55)
# LL.prettyPrint()
LL1 = LinkedList()
LL1.insert_list(lst,1)
LL1.prettyPrint()
# LL2 = LinkedList()
# LL2.insert_list(lst)
# LL2.prettyPrint()
LL1.insert_after_node(4.5,4)
LL1.prettyPrint()
LL1.delete_node(4.5)
LL1.prettyPrint()
