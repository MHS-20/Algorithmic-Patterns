def dfs(graph, source): 
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)

def recursiveDFS(graph, source):
    print(source)
    for neighbor in graph[source]:
        recursiveDFS(graph, neighbor)
