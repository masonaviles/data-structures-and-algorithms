class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self):
        self.root = None

def breadth_first_fizzbuzz(tree):
    # if there is nothing
    if tree.root is None:
        return
    # Create an empty queue
    q = []
    # Enqueue Root
    q.append(tree.root)

    new_tree = Tree()
    # while there are things in the queue loop
    # while (len(q) > 0):
    while q:
        # do stuff
        fizzbuzz_value = fizzbuzz(q[0].value)
        print(fizzbuzz_value)
        new_node = Node(fizzbuzz_value)

        node = q.pop(0)
        # Enqueue each child
        for child in node.children:
            q.append(child)

def fizzbuzz(root_value):
    if root_value % 15 == 0:
        root_value = "FizzBuzz"
        return root_value
    elif root_value % 3 == 0:    
        root_value = "Fizz"
        return root_value
    elif root_value % 5 == 0:        
        root_value = "Buzz"
        return root_value
    return str(root_value)


if __name__ == "__main__":
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)

    """
                1
            2          5
        3      4     6 7 8
    """

    one.children = [two, five]
    two.children = [three, four]
    five.children = [six, seven, eight]
    kt = Tree()
    kt.root = one

    bf_collection = breadth_first_fizzbuzz(kt)
    print(bf_collection)