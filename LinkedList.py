class Node: 
    def __init__ (self, data = None, next = None):
        self.data = data 
        self.next = next

class LinkedList:
    def __init__ (self):    #constructor 
        self.head = None
		
        
    #Insert node at beginning of Linked List
    def insert_beginning(self, data):  
        node = Node(data, self.head)
        self.head = node
		
        
    #Delete Node From beginning of Linked List    
    def remove_beginning(self):
        temp = self.head
        self.head = temp.next
		
        
    #Insert Node at end of Linked List
    def insert_end(self, data):
        if self.head == None:
            node = Node(data)
            self.head = node
            return
        node = Node(data)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node
        
        
		
    #Insert Node at specific Index of Linked List
    def add_middle(self, index, data):
        if self.head == None or index > self.length_list() or index < 0:
            return
        if index == 0:
            self.insert_beginning(data)
            return
        temp = self.head
        idx = 0
        while idx < (index-1):
            if temp.next == None:
                return
            temp = temp.next
            idx += 1
        temp.next = Node(data, temp.next)
        return
    
	
    #Remove Node from Specific Index of Linked List    
    def remove_middle(self, index):
        if self.head == None or index > self.length_list() or index < 0:
            return
        if index == 0:
            self.remove_beginning()
            return
        temp = self.head
        idx = 0
        while idx < (index-1):
            if temp.next == None:
                return
            temp = temp.next
            idx += 1
        temp.next = temp.next.next
        return 
    
	
    #Remove Node by its Value 
    def remove_value(self, value):
        if self.head == None:
            return 
        temp = self.head
        counter = 0
        while temp:
            if temp.data == value:
                self.remove_middle(counter)
                return
            counter += 1
            temp = temp.next
        return

	
    #Return Length of Linked List
    def length_list(self):
        temp = self.head
        counter = 0
        while temp:
            counter += 1
            temp = temp.next
        return counter
            
		
    #Print Linked List
    def printlist(self):
        if self.head == None:
            return "List is empty"
        temp = self.head
        list = ""
        while temp:
            list += str(temp.data) + "-->"
            temp = temp.next
        print(list)
        
# Main Function for Testing our Linked List

# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insert_beginning(2)
#     ll.insert_beginning(1)
#     ll.printlist()
#     ll.insert_end(3)
#     ll.printlist()
#     ll.insert_end(4)
#     ll.printlist()
#     print(ll.length_list())
#     ll.remove_middle(1)
#     ll.printlist()
#     ll.add_middle(1, 2)
#     ll.add_middle(0, 0)
#     ll.printlist()    
#     ll.remove_beginning()
#     ll.printlist()
#     ll.remove_value(2)
#     ll.printlist()
    
    
