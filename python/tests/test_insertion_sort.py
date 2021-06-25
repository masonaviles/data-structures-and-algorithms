from code_challenges.insertion_sort.insertion_sort import InsertionSort


def test_import():
    assert InsertionSort

# give: [8,4,23,42,16,15]
# get: [4, 8, 15, 16, 23, 42]

def test_sort():
    actual = InsertionSort([8,4,23,42,16,15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected