#!/usr/bin/env python
"""Merge k Sorted Lists"""

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listToLinkedlist(lst: List[int]) -> ListNode:
    """List to linkedlist"""
    head = ListNode(lst[0])
    cur = head
    for i in lst[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """Merge k sorted list using brute force"""
    vals = []
    for head in lists:
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

    if not vals:
        return None

    vals.sort()

    return listToLinkedlist(vals)

def LinkedList(head: Optional[ListNode]):
    """Return List"""
    lst = []
    curr = head
    while curr:
        lst.append(curr.val)
        curr = curr.next
    return lst

if __name__ == "__main__":
    list1 = listToLinkedlist([1, 4, 5])
    list2 = listToLinkedlist([1, 3, 4])
    list3 = listToLinkedlist([2, 6])
    lists = [list1, list2, list3]

    result = mergeKLists(lists)
    print(LinkedList(result))
