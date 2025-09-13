def zip_list(head1, head2):
    count = 0
    tail = head1
    head1 = head1.next

    while head1 is not None and head2 is not None:
        if count % 2 == 0:
            tail.next = head2
            head2 = head2.next
        else:
            tail.next = head1
            head1 = head1.next
        count += 1
        tail = tail.next

    if head2 is not None:
        tail.next = head2

    if head1 is not None:
        tail.next = head1

    return head1


def recursive_zip(head1, head2):
    if head1 is None and head2 is None: 
        return None
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    head1.next = recursive_zip(head2, head1.next)
    return head1

