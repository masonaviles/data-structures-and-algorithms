from stacks_and_queues.stacks_and_queues import Stack, Queue, Node

# STACK TESTS

def test_stack_defined():
    assert Stack

def test_stack_has_top():
    s = Stack()
    assert s.top is None

# Can successfully push onto a stack
def test_push_single():
    s = Stack()
    s.push("tea")
    actual = s.top.value
    expected = "tea"
    assert actual == expected

# Can successfully push multiple values onto a stack
def test_push_multiple():
    s = Stack()
    s.push("tea")
    s.push("coffee")
    s.push("juice")
    actual = s.top.value
    expected = "juice"
    assert actual == expected

# Can successfully pop off the stack
def test_pop_single():
    s = Stack()
    s.push("tea")
    actual = s.pop()
    expected = "tea"
    assert actual == expected

# Can successfully empty a stack after multiple pops
def test_empty_stack_multi_pop():
    s = Stack()
    s.push("tea")
    s.push("coffee")
    s.push("juice")
    s.pop()
    s.pop()
    actual = s.pop()
    expected = "tea"
    assert actual == expected


# Can successfully peek the next item on the stack
# Can successfully instantiate an empty stack
# Calling pop or peek on empty stack raises exception


# QUEUE TESTS

def test_queue_defined():
    assert Queue

def test_queue_has_front():
    q = Queue()
    assert q.front is None

def test_queue_has_back():
    q = Queue()
    assert q.back is None

# Can successfully enqueue into a queue
# Can successfully enqueue multiple values into a queue
# Can successfully dequeue out of a queue the expected value
# Can successfully peek into a queue, seeing the expected value
# Can successfully empty a queue after multiple dequeues
# Can successfully instantiate an empty queue
# Calling dequeue or peek on empty queue raises exception