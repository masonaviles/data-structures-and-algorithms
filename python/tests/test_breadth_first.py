from code_challenges.breadth_first_binary_tree.breadth_first import (breadth_first, Node)


def test_import():
    assert breadth_first

def test_function():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    actual = breadth_first(root)
    expected = [1,2,3,4,5]
    assert actual == expected
