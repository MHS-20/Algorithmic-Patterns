# find the shortest path from src to dst
from collections import deque, defaultdict
def toAdjacent(edges):
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return dict(adj)

def shortest_path(edges, src, dst):
    graph = toAdjacent(edges)
    queue = deque([(src,0)])
    visited  = set()

    while len(queue) > 0:
        current, count = queue.popleft()
        
        if current in visited: 
            continue
        visited.add(current)
        
        if current == dst: 
            return count

        for neighbor in graph[current]:
            queue.append((neighbor,count+1))
    return -1
