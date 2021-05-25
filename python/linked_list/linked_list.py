class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, search_value):
        current = self.head
        while current:
            if current.value == search_value:
                return True
            current = current.next
        return False

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


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next