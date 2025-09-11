from tree_node import TreeNode

def iterativeDFS(root: TreeNode) -> list[int]:
    if root is None: 
        return []

    stack = [root]
    res = []
    
    while(len(stack) > 0):
        node = stack.pop()
        res.append(node.val)

        if node.right:
            stack.append(node.right)
        
        if node.left:
            stack.append(node.left)

    return res
