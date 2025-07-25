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
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy

    while head and head.next:
        first = head
        second = head.next

        prev.next = second
        first.next = second.next
        second.next = first

        prev = first
        head = first.next

    return dummy.next

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
