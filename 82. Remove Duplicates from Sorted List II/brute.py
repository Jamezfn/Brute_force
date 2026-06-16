#!/usr/bin/env python

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def listToLinked(self, nums: List) -> Optional['ListNode']:
        if not nums:
            return None

        head = ListNode(nums[0])
        
        cur = head
        for num in range(1, len(nums)):
            cur.next = ListNode(nums[num])
            cur = cur.next

        return head

    def LinkedToList(self, head: Optional['ListNode']) -> List:
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next

        return nums

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = {}

        cur = head

        while cur:
            freq[cur.val] = freq.get(cur.val, 0) + 1
            cur = cur.next
        
        dummy = ListNode(0)
        tail = dummy
        cur = head

        while cur:
            if freq[cur.val] == 1:
                tail.next = ListNode(cur.val) 
                tail = tail.next
            cur = cur.next

        return dummy.next


nums = [1, 2, 3, 3, 4, 4, 5]

node = ListNode()

head = node.listToLinked(nums)

sol = Solution()
result = sol.deleteDuplicates(head)

print(node.LinkedToList(result))
