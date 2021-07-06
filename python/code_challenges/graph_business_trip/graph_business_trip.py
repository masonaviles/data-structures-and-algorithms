# Write a function called business trip
# Arguments: graph, array of city names
# Return: cost or null

def business_trip(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = business_trip(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths