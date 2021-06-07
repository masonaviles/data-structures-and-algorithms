class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:

    def __init__(self, node):
        self.root = None
        self.left = node.left
        self.right = node.right
        self.value = node.value

    def getRoot(self):
        return self.root

    # print function
    def PrintTree(self):
        print(self.value)

    # A function to do inorder tree traversal
    def inOrder(self):
        if self:
            # First recur on left child
            self.inOrder(self.left)
            # then print the data of node
            print(self.value)
            # now recur on right child
            self.inOrder(self.right)

    # A function to do postorder tree traversal
    def postOrder(self):
        if self:
            # First recur on left child
            self.postOrder(self.left)
            # the recur on right child
            self.postOrder(self.right)
            # now print the data of node
            print(self.value)

    # A function to do preorder tree traversal
    def preOrder(self):
        if self:
            # First print the data of node
            print(self.value),
            # Then recur on left child
            self.preOrder(self.left)
            # Finally recur on right child
            self.preOrder(self.right)