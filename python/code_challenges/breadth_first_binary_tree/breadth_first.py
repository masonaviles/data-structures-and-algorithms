class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def breadth_first(root):
    # Base Case
    if root is None:
        return
    # Create an empty queue
    q = []
    bf_list = []
    # Enqueue Root
    q.append(root)
    # while there are things in the queue loop
    while(len(q) > 0):
        # add front of queue to list and
        # remove it from queue
        bf_list.append(q[0].value)
        node = q.pop(0)
        # Enqueue left child
        if node.left is not None:
            q.append(node.left)
        # Enqueue right child
        if node.right is not None:
            q.append(node.right)
    return bf_list