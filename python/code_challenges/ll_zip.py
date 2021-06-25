def zipLists(list1, list2):
    """ a function to zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.

    Args:
        list1 (list): a linked list to zip in other ll
        list2 (list): a linked list to zip in other ll

    Output -> a single linked list
    """

    # return = [*transform* *iteration* *filter* ] 
    # transform -> sub[item]
    # iteration -> for item in range
    # filter -> (loop) for sub in [list1, list2]

    # lst1 = [1, 2, 3]
    # lst2 = ['a', 'b', 'c']

    return [sub[item] for item in range(len(list2))
        for sub in [list1, list2]]
        # [ [0] of list1, [0] of list2 ] -> [ 1, 'a' ]
        # [ [1] of list1, [1] of list2 ] -> [ 1, 'a', 2, 'b' ]
        # [ [2] of list1, [2] of list2 ] -> [1, 'a', 2, 'b', 3]
        # [ 1, 'a' ]
      
# Test code
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
print(zipLists(lst1, lst2))

# class zipLists(list1, list2):
#     list1_curr = list1.head
#     list2_curr = list2.head

#     # Save Next in Var's
#     while list1_curr and list2_curr:
#         list1_next = list1_curr.next
#         list2_next = list2_curr.next
#         # Make list2 current as next of list1
#         list1_curr.next = list2_next
#         list2_curr.next = list1_next
#         # Update current to next iteration
#         list1_curr = list2_next
#         list2_curr = list1_next
#     list1.head = list1_curr