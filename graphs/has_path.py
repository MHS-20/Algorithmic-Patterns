# say if a graph has a path from src to dst
from collections import deque

def has_path_dfs(graph, src, dst):
    if src == dst:
        return True
    for neighbor in graph[src]:
        res = has_path_dfs(graph, neighbor, dst)
        if res is True:
            return True
    return False

def has_path_bfs(graph, src, dst):
    queue = deque(src)
    while len(queue) > 0:
        current = queue.popleft()
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False
