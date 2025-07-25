#!/usr/bin/env python

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def toLinkedList(lst: Optional[List[int]]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    """Swap nodes using brute force"""
    if not head or not head.next:
        return head

    first = head
    second = head.next

    first.next = swapPairs(second.next)
    second.next = first

    return second

def toList(head: Optional[ListNode]) -> Optional[List]:
    """Linked list to list"""
    res = []
    current = head
    while current:
        res.append(current.val)
        current = current.next
    return res

if __name__ == '__main__':
    lst = [1, 2, 3, 4]
    linkedlist = toLinkedList(lst)
    head = swapPairs(linkedlist)
    print(toList(head))
