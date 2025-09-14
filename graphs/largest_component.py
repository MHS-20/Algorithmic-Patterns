# return the count of nodes for the largest component
def largest_component(graph):
    visited = set()
    count = 0
    for node in graph:
        if node in visited: 
            continue
        res = dfs(graph, node, visited)
        count = max(res, count)
    return count

def dfs(graph, current, visited):
    count = 0
    visited.add(current)
    for neighbor in graph[current]:
        if neighbor not in visited:
            count += dfs(graph, neighbor, visited)
    return count+1
