# say if there is path from src to dst 
# in an undirected graph

from collections import defaultdict, deque
def convertToAdjacent(edges):
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return dict(adj)

def undirected_path_bfs(edges, src, dst):
    graph = convertToAdjacent(edges)
    queue = deque(src)
    visited = set()

    while len(queue) > 0: 
        current = queue.popleft()
        visited.add(current)
        if current == dst:
            return True
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
    return False


def undirected_path_dfs(edges, src, dst):
    def helper(graph, src, dst, visited):
        visited.add(src)
        if src == dst:
            return True

        for neighbor in graph[src]:
            if neighbor not in visited:
                if helper(graph, neighbor, dst, visited):
                    return True
        return False
    graph = convertToAdjacent(edges)
    return helper(graph, src, dst, set())
