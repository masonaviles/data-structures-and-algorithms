class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)
        # old_top = self.top
        # new_top = Node(value)
        # self.top = new_top
        # new_top.next = old_top

    def pop(self):
        if not self.top:
            raise InvalidOperationError(
                "Method not allowed on empty collection"
            )
        val = self.top.value
        self.top = self.top.next
        return val

    def is_empty(self):
        return self.top is None
    
    def peek(self):
        if not self.top:
            raise InvalidOperationError(
                "Method not allowed on empty collection"
            )
        return self.top.value

class Queue:
    def __init__(self):
        self.front = None
        self.back =  None

    def enqueue(self, value):
        new_data = Node(value)
        if self.front is None:
           self.front = new_data
           self.back = self.front
        else:
           self.back.next = new_data
           self.back = new_data

    def dequeue(self):
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
           self.back is None
        return value

    def peek(self):
        if not self.front:
            raise InvalidOperationError(
                "Method not allowed on empty collection"
            )
        return self.front.value

    def isEmpty(self):
        return self.front is None