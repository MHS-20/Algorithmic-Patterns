# sum all values in the tree

def tree_sum(root)->int:
    if root is None: 
        return 0

    s1 = tree_sum(root.left)
    s2 = tree_sum(root.right)
    return s1 + s2 + root.val
