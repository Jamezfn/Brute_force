#!/usr/bin/env python
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """Merge two sorted list using brute force"""
    vals: List[int] = []
    cur = list1
    while cur:
        vals.append(cur.val)
        cur = cur.next

    cur = list2
    while cur:
        vals.append(cur.val)
        cur = cur.next

    if not vals:
        return None

    vals.sort()

    head = ListNode(vals[0])
    cur = head
    for val in vals[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

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
