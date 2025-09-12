# find the smallest value in the tree

def tree_min(root): 
    if root is None: 
        return 10000

    min1 = tree_min(root.left)
    min2 = tree_min(root.right)

    return min(min1,min2,root.value)

