#!/usr/bin/env python
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """Merge two sorted list using Iterative two‑pointer merge"""
    dummy = tail = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            tail.next, list1 = list1, list1.next
        else:
            tail.next, list2 = list2, list2.next
        tail = tail.next
    tail.next = list1 or list2
    return dummy.next

def to_list(node: Optional[ListNode]) -> List[int]:
    """Convert nodes to list"""
    out = []
    cur = node
    while cur:
        out.append(cur.val)
        cur = cur.next

    return out


if __name__ == "__main__":
    # list1 = [1,2,4], list2 = [1,3,4]
    a = ListNode(1, ListNode(2, ListNode(4)))
    b = ListNode(1, ListNode(3, ListNode(4)))
    merged = mergeTwoLists(a, b)
    print(to_list(merged))
