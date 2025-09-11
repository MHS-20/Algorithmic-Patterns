from tree_node import TreeNode

def recursiveDFS(root) -> list[int]:
    if root is None: 
        return []

    res = [root.val]
    left_vals = recursiveDFS(root.left)
    right_vals = recursiveDFS(root.right)
    res.extend(left_vals)
    res.extend(right_vals)
    return res
