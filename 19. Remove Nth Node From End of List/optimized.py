#!/usr/bin/env python
"""Remove Nth Node From End of List using brute force"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    first = dummy
    second = dummy

    for _ in range(n+1):
        first = first.next

    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next

def linked_list_to_array(head):
    result = []
    cur = head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result

hd = array_to_linked_list([1,2,3,4,5])
sl = removeNthFromEnd(hd, 2)
ls = linked_list_to_array(sl)

print(ls)
