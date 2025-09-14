# count how many separated connected-components are in the graph
def connected_components(graph):
    count = 0
    visited = set()
    for node in graph:
        if node in visited:
            continue
        dfs(graph, node, visited)
        count+=1
    return count

def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited: 
            dfs(graph, neighbor, visited)
