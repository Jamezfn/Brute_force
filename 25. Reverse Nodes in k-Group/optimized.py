#!/usr/bin/env python
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def toLinkedList(lst: Optional[List]) -> ListNode:
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """Reverse Nodes in a k-Group using brute force"""
    if k <= 1 or not head:
        return head

    dummy = ListNode()
    dummy.next = head

    grp_prev = dummy
    while True:
        kth = grp_prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next

        grp_next = kth.next
        prev, curr = grp_next, grp_prev.next
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        tail = grp_prev.next
        grp_prev.next = kth
        grp_prev = tail


def tolist(head: Optional[ListNode]) -> Optional[List]:
    lst = []
    curr = head
    while curr:
        lst.append(curr.val)
        curr = curr.next
    return lst

if __name__ == '__main__':
    head = toLinkedList([1,2,3,4,5])
    rev = reverseKGroup(head, 2)
    print(tolist(rev))
