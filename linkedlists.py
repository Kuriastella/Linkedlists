class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print("-->".join(elements)+"-->")

my_list = LinkedList() 
print(my_list.is_empty())

my_list.head = Node(10)
my_list.head.next = Node(20)
my_list.head.next.next = Node(30)

my_list.display()
print(my_list.is_empty())

#Append at the end
    def append(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
            current.next = new_node

#insert at the beggining of the Linked list
    def insert_at_begginig(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

#Insert at specific position(0-based index)    
    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_position(data)
            return 

        new_node = Node(data)
        current = self.head
        count = 0

        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of range")
            return

        new_node.next = current.next
        current.next = new_node    
        
#Delete first occurrence of value, return True if deleted, False if not found
   
    def delete_by_value(self, value):
        if self.is_empty():
            return False 
        #Check if head contains the value
        if self.head.data == value:
            self.head = self.head.next 
            return True
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return True
            current = current.next
        return False 
    
#Find element, return index or -1 if not found
    def search(self, value):
        current = self.head
        index = 0
        
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1
    