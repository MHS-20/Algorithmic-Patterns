from collections import deque
def bfs(graph, source):
    queue = deque(source)
    while len(queue) > 0: 
        current = queue.popleft()
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)
