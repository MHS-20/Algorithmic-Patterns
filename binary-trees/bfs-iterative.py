from tree_node import TreeNode
from collections import deque

def iterativeBFS(root) -> list[int]:
    if root is None: 
        return []
    res = []
    queue = deque(root)

    while len(queue) > 0: 
        node = queue.popleft()
        res.append(node.val)

        if node.left is not None: 
            queue.append(node.left)

        if node.right is not None: 
            queue.append(node.right)
    return res
