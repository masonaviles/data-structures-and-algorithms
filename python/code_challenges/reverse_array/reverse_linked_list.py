def reverse_list(ll):
    """Reverses a linked list
    Args:
        ll: linked list
    Returns:
        linked list in reversed form
    """
    # put your function implementation here

    new = []
    for i in ll:
        new.insert(0, i)
 
    return new

def reverse(l):
    new = []
    for i in l:
        new.insert(0, i)
    return new