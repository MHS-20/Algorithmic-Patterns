def list_to_array(head) -> list[int]:
    current = head
    arr = []
    while current is not None:
        arr.append(current.val)
        current = current.next
    return arr


def recursive_to_array(head):
    arr = []
    helper(head, arr)
    return arr

def helper(head, arr):
    if head is None:
        return
    arr.append(head.val)
    helper(head.next, arr)
