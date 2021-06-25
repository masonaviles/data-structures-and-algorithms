class LinkedList:

    def __init__(self, head=None, values=None):
        self.head = head
        if values:
            for value in values:
                self.insert(value)
        
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
    def __str__(self):
        string = ''
        current = self.head
        while current:
            string += f'{current.value} --> '
            current = current.next
        string += 'None'
        return string

    def append(self, value):
      current = self.head
      while current:
        if current.next == None:
          current.next = Node(value)
          break
        current = current.next

    def insertBefore(self, value, new_value):
      current = self.head
      previous = None
      while current:
        if self.head.value == value:
          self.insert(new_value)
          break
        if current.value == value:
          previous.next = Node(new_value, current)
          break
        previous = current
        current = current.next

    def insertAfter(self, value, new_value):
      current = self.head
      insert_before_this = current.next
      while current:
        if self.head.value == value:
          self.insert_before(insert_before_this.value, new_value)
          break
        if current.value == value:
          current.next = Node(new_value, insert_before_this)
          break
        current = current.next
        insert_before_this = current.next
    # Input -> takes a number, k
    # Output -> the node’s value that is [k] from the end of the linked list

    def nthFromLast(self, k): # 5
        current = self.head
        length = 0

        # walk and count
        # count the nodes in the linked list
        while current:
            current = current.next
            length = length + 1
         
        # if the total number of nodes(length) is more than or equal to `k`
        if length >= k:
            # return (legngth-k+1)'th node from the beginning's value
            current = self.head
            for i in range(length - k):
                current = current.next

        return current.data

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


