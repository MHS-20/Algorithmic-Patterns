def reverse_list(head) -> ListNode:
    previous = None
    current = head
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous

def recursive_reverse(head) -> ListNode: 
    def helper(current, prev):
        if current is None: 
            return prev
        next = current.next
        current.next = prev
        prev = current
        current = next 
        return helper(current, prev)
    return helper(head, None)

