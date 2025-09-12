def sum_list(head) -> int:
    current = head
    sum = 0
    while current is not None: 
        sum += current.val
        current = current.next
    return sum

def  recursiveSumList(head)->int:
    if head is None:
        return 0

    return head.val + recursiveSumList(head.next)
