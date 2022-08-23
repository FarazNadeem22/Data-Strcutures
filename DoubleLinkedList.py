######################
# Double Linked List #
#    Muhammd Ali     #
#    8/14/2022       #
######################

#imports 
from hashlib import new
import sys

# Classes 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class doubleLinkList:
    def __init__(self):
        self.head = None
          
    def print(self, forward = True):
        try:
            if forward:
                #check if linked List in empty
                if self.head is None:
                    print("Linked List is empty")
                else:
                    #if not empty
                    ptr = self.head
                    while ptr is not None:
                        print(ptr.data,"->",end=" ")
                        ptr = ptr.next
                print("\n")
            else:
                if self.head is None:
                        print("Linked List is empty")
                else:
                    #if not empty
                    ptr = self.head
                    #get to the last position
                    while ptr.next is not None:
                        ptr = ptr.next 
                    while ptr is not None:
                        print(ptr.data,"->",end=" ")
                        ptr = ptr.prev
                print("\n")
        except:
            print("Something went wrong")       

    def prettyPrint(self, forward = True):
        try:
            if forward:
                ptr = self.head   
                while ptr and ptr.next:
                    sys.stdout.write(str(ptr.data)+"->")
                    ptr = ptr.next       
                if ptr:
                    print(ptr.data)
                else:
                    print("Empty List")
            else:
                if self.head is None:
                    print("Empty List")
                else:
                    ptr = self.head
                    #go to last node
                    while ptr.next is not None:
                        ptr = ptr.next
                    # at last node 
                    while ptr and ptr.prev:
                        sys.stdout.write(str(ptr.data)+"<-")
                        ptr = ptr.prev 
                    print(ptr.data)
        except:
            print("Something Went Wrong")

    def insert_empty(self,data):
        try:
            if self.head is None:
                new_node = Node(data)
                self.head = new_node
            else:
                print("Linked List is not empty")
        except:
            print("OOPs Something went wrong")
    
    def insert_start(self,data):
        try:
            if self.head is None:
                self.insert_empty(data) 
            else:
                #Create New Node
                new_node = Node(data)
                #set ptr to head 
                ptr = self.head
                #set back pointer to new node 
                ptr.prev = new_node
                #set head pointer to new node as it is at the start of the list 
                self.head = new_node
                #Set make forward pointer of new node point to ptr (previous head node)
                new_node.next = ptr
                #As now new node is head node set previous pointer to NULL
                new_node.prev = None
        except:
            print("Something Went Wrong")
            
    def insert_end(self,data):
        try:
            #Check if List in empty 
            if self.head is None:
                self.insert_empty(data)
            else:
                #set pointer to head node
                ptr = self.head
                #go to last node 
                while ptr.next:
                    ptr =ptr.next
                #at Last node 
                new_node = Node(data)
                ptr.next = new_node
                tmp = ptr
                ptr = ptr.next
                ptr.prev = tmp
                del(tmp)   
        except:
            print("Something Went Wrong")    

    def insert_list_end(self, lst):
        try:
            for element in lst:
                self.insert_end(element)             
        except:
            print("Something Went Wrong")
            
    def insert(self, data, ptr):
        new_node = Node(data)
        new_node.next = ptr.next
        new_node.prev = ptr
        ptr.next = new_node
        
    def insert_after(self,data,target):
        try:
            if self.head is None:
                print("Empty List")
            else:
                ptr = self.head
                while ptr.data != target:
                    ptr = ptr.next
                #target found
                self.insert(data,ptr)       
        except:
            print("Target '{}' not found in list")
    
    def insert_before(self,data,target):
        try:
            if self.head is None:
                print("Empty List")
            else:
                ptr = self.head
                while ptr.next.data != target:
                    ptr = ptr.next
                #target found
                self.insert(data,ptr)       
        except:
            print("Target '{}' not found in list".format(target))
        
    def delete_before(self,target):
        try:
            if self.head is None:
                print("Empty List")
            else:
                ptr = self.head
                while ptr.next.data != target:
                    ptr = ptr.next
                #target found
                self.delete_node(ptr)       
        except:
            print("Target '{}' not found in list".format(target))
    
    def delete_after(self,target):
        try:
            if self.head is None:
                print("Empty List")
            else:
                ptr = self.head
                while ptr.data != target:
                    ptr = ptr.next
                #target found
                self.delete_node(ptr.next)       
        except:
            print("Target '{}' not found in list".format(target))
    
    def delete_node(self, ptr):
        try:
            if ptr.prev is None and ptr.next is None:
                #Only Node
                self.head = None
            elif ptr.prev is None and ptr.next:
                #first Node
                self.head = ptr.next
                
            elif ptr.prev and ptr.next is None:
                #Last Node
                tmp = ptr.prev
                tmp.next = None
            else:
                #some middle node
                tmp = ptr.prev
                tmp.next =ptr.next
                ptr.next.prev = tmp  
        except:
            print("Something went wrong")
        
    def delete_target(self,target):
        try:
            if self.head is None:
                print("Empty list")
            else:
                ptr = self.head
                while ptr.data != target:
                    ptr = ptr.next
                #target found
                self.delete_node(ptr)
        except:
            print("target'{}' not found in list".format(target))
                    
DLL = doubleLinkList()
# DLL.insert_empty(50)
# #DLL.print()
# DLL.insert_start(10)
# DLL.insert_start(5)
# DLL.prettyPrint()
# DLL.insert_end(60)
# DLL.prettyPrint()
# DLL.prettyPrint(0)
lst = [20,40,50,100,200,300,400,500,600]
DLL1 = doubleLinkList()
DLL1.insert_list_end(lst)
DLL1.prettyPrint()
DLL1.insert_before(250,200)
DLL1.prettyPrint()
DLL1.delete_target(250)
DLL1.prettyPrint()
DLL1.delete_before(300)
DLL1.prettyPrint()
DLL1.delete_after(100)
DLL1.prettyPrint()
DLL1.prettyPrint(0)