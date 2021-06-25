class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):

        # while stack1 isn't empty
        while self.stack1:
            # push everything to stack2
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()

        # push value to stack1
        self.stack1.append(value)

        # push everything back to stack1
        while self.stack2:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()

    def dequeue(self):

        # if stack1 is empty, return false
        if len(self.stack1) == 0:
            return False

        # pop from stack1
        dequeue_value = self.stack1[-1]
        self.stack1.pop()
        return dequeue_value