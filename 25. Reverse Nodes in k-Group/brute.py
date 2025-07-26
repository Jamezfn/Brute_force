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
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    
    n = len(nodes)
    for i in range(0, n, k):
        if i + k <= n:
            nodes[i:i+k] = reversed(nodes[i:i+k])

    for i in range(n-1):
        nodes[i].next = nodes[i+1]
    nodes[-1].next = None
    return nodes[0]


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
