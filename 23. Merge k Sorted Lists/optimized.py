#!/usr/bin/env python
"""23. Merge k Sorted Lists"""
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listToLinkedList(lst: List[int]) -> ListNode:
    """List to linkedlist"""
    head = ListNode(lst[0])
    cur = head
    for i in lst[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """Merge k sorted lists using divide and conquer"""
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    def merge(lists: List[Optional[ListNode]], start: int, end: int) -> Optional[ListNode]:
        if start == end:
            return lists[start]
        mid = (start + end) // 2
        l = merge(lists, start, mid)
        r = merge(lists, mid + 1, end)
        return mergeTwoLists(l, r)

    return merge(lists, 0, len(lists) - 1)


if __name__ == '__main__':
    list1 = listToLinkedList([1, 4, 5])
    list2 = listToLinkedList([1, 3, 4])
    list3 = listToLinkedList([2, 6])

    merged = mergeKLists([list1, list2, list3])
    cur = merged
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")

