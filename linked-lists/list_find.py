def list_find(head, target)-> bool:
    current = head 
    while current is not None: 
        if current.val == target:
            return True
        current = current.next
    return False

def list_find_recursive(head, target)->bool: 
    if head is None: 
        return False
    if head.val == target:
        return True
    return list_find_recursive(head.next, target)
