# say if a given value is in the tree
from collections import deque
def include_bfs(root, target) -> bool:
    if root is None: 
        return False

    queue = deque(root)

    while len(queue) > 0: 
        node = queue.popleft()
        
        if node.val == target: 
            return True

        if node.left is not None: 
            queue.append(node.left)
        
        if node.right is not None: 
            queue.append(node.right)
            
    return False
