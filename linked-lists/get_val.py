def get_val(head, index):
    if head is None:
        return None

    current = head
    count = 0
    
    while current is not None:
        if index == count:
            return current.val
        current = current.next
        count += 1
    return None


def recursive_get_val(head, index):
    if head is None: 
        return None
    if index == 0:
        return head.val
    return recursive_get_val(head.next, index - 1)
