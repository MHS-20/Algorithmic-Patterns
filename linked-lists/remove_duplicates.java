/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
  public ListNode deleteDuplicates(ListNode head) {
    ListNode current;
    ListNode prev;

    if (head == null)
      return null;

    current = head.next;
    prev = head;

    while (current != null) {
      if (current.val == prev.val) {
        prev.next = current.next;
        current = current.next;
      } else {
        prev = current;
        current = current.next;
      }
    }

    return head;
  }

  public ListNode recursiveDeleteDuplicates(ListNode head) {
    helper(head.next, head);
    return head;
  }

  public void helper(ListNode current, ListNode prev) {
    if (current == null)
      return;

    if (current.val == prev.val) {
      prev.next = current.next;
      helper(current.next, prev);
    } else {
      prev = current;
      helper(current.next, prev);
    }
  }

}
