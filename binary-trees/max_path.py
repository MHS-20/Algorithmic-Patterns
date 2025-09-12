# find the path root to leaf that has the maximum sum

def max_path(root):
    if root is None:
        return  -10000

    if root.left is None and root.right is None:
        return root.value

    max1 = max_path(root.left)
    max2 = max_path(root.right)

    return root.val + max(max1, max2)
