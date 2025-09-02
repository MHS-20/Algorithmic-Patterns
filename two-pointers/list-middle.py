class Node: 
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def  list_middle(head: Node) -> int: 
    fast = slow = head 
    

    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
    return slow.val # with even list, it returns the second middle
