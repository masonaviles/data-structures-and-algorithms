from code_challenges.graph_depth_first.graph_depth_first import Graph

def test_exist():
    assert Graph.depth_first
def test_can_traverse():
    graph = Graph()
    graph_list = {
        '5' : ['3','7'],
        '3' : ['2', '4'],
        '7' : ['8'],
        '2' : [],
    }
    actual = sorted(graph.depth_first(graph_list, '5'))
    expected = sorted(['5', '3', '7', '2', '8', '4'])
    assert actual == expected
def test_can_traverse_short():
    graph = Graph()
    graph_list = {
        '5' : ['3'],
        '3' : [],
    }
    actual = sorted(graph.depth_first(graph_list, '5'))
    expected = sorted(['5', '3'])
    assert actual == expected
def test_empty_graph():
    graph = Graph()
    graph_list = {}
    actual = sorted(graph.depth_first(graph_list, '5'))
    expected = []
    assert actual != expected
def test_empty_one_value():
    graph = Graph()
    graph_list = {
        '5' : []
    }
    actual = graph.depth_first(graph_list, '5')
    expected = ['5']
    assert actual == expected