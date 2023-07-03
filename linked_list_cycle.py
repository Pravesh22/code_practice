"""
-- Created by Pravesh Budhathoki
-- Created on 2023-06-14
"""
from typing import Optional


# 141. Linked List Cycle
# For question please go through this link.
# https://leetcode.com/problems/linked-list-cycle/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        start = head
        end = head.next
        while start is not None and end is not None and end.next is not None:
            if start == end.next:
                return True
            start = start.next
            end = end.next.next
        return False


if __name__ == '__main__':
    _head = [1]
    solution = Solution()
    solution.hasCycle(_head)
