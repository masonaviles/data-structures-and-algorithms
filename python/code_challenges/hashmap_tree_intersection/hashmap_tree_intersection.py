class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

class BinaryTree:

    def __init__(self, root=None):
        self.root = root

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
    # root -> left -> right
    def preOrder(self):
        if self:
            # First print the data of node
            print(self.value)
            # Then recur on left child
            self.preOrder(self.left)
            # Finally recur on right child
            self.preOrder(self.right)

lst1= BinaryTree()
list2=BinaryTree()

def find_common_values(tree1, tree2):
    lst1 = tree1.preOrder()
    lst2 = tree2.preOrder()
    return [item for item in lst1 if item in list2]