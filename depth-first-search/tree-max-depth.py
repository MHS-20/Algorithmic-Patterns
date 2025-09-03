class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def tree_max_depth(root: Node) -> int:
    def dfs(root):
        if not root:
            return 0
        return max(dfs(root.left), dfs(root.right)) + 1
    return  dfs(root) -1 if not root else 0
    
