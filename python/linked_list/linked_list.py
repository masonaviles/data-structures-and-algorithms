class LinkedList:
    def __init__(self):
        self.head = None
        
    # return the whole list in the linked list
    def to_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values

    # traverse list and check to see if value is in a LinkedList
    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    # insert at the beginning
    def insert(self, value):
        # old_head = self.head
        # node = Node(value, old_head)
        self.head = Node(value, self.head)
        # node.next = old_head

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next