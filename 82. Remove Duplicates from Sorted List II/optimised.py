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
        dummy = ListNode(0, head)
        prev = dummy
        cur = head

        while cur:
            if cur.next and cur.val == cur.next.val:
                val = cur.val

                while cur.val == val:
                    cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next

        return dummy.next


nums = [1, 2, 3, 3, 4, 4, 5]

node = ListNode()

head = node.listToLinked(nums)

sol = Solution()
result = sol.deleteDuplicates(head)

print(node.LinkedToList(result))
