# say if a value in the tree
def include_dfs(root, target)->bool:
    if root is None: 
        return False

    if  root.val == target: 
        return True

    res1 = include_dfs(root.left, target)
    res2 = include_dfs(root.right, target)

    return res1 or res2

