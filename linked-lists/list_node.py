class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head): 
    current = head
    while current is not None: 
        print(current.val)
        current = current.next

def recursivePrint(head):
    if head is not None: 
        print(head.val)
        recursivePrint(head.next)
