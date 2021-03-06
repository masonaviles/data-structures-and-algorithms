def multiBracketValidation(input):
    open_brackets = [ "[", "{", "(" ]
    close_brackets = [ "]", "}", ")" ]
    stack = []
    for char in input:
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            # if we encounter a closed bracket but there was never an open bracket in the stack to begin with, then False
            if len(stack) <= 0:
                return False
            # if what we popped from stack (which should be all opens) doesn't match the close bracket we just found, then False
            if open_brackets.index(stack.pop()) != close_brackets.index(char):
                return False
    return True