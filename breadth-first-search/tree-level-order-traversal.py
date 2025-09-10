# return a list of lists, each list contains the value of each level
from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def level_order_traversal(root: Node) -> list[list[int]]:
    res = []
    queue = deque([root])
    while len(queue) > 0:
        n = len(queue)
        new_level = []
        for _ in range(n):
            node = queue.popleft()
            new_level.append(node.val)
            for child in [node.left, node.right]:
                if child is not None:
                    queue.append(child)
        res.append(new_level)
    return res
