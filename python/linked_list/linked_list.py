class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        # initialization here
        pass

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
