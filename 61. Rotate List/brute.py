#!/usr/bin/env python

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def listToLinkedList(self, nums: List[int]) -> Optional['ListNode']:
        if not nums: return None

        head = ListNode(nums[0])
        cur = head
        for num in nums[1:]:
            cur.next = ListNode(num)
            cur = cur.next

        return head

    def LinkedListToList(self) -> List[int]:
        nums = []
        cur = self

        while cur:
            nums.append(cur.val)
            cur = cur.next
        
        return nums


    def rotateRight(self, head: Optional['ListNode'], k: int) -> Optional['ListNode']:
        if not head:
            return head

        length, tail = 1, head

        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        
        newHead = cur.next
        cur.next = None
        tail.next = head

        return newHead


h = [1,2,3,4,5]
node = ListNode()
head = node.listToLinkedList(h)
r = node.rotateRight(head, 2)
print(r.LinkedListToList())

