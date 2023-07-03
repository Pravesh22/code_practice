"""
-- Created by Pravesh Budhathoki
-- Created on 2023-06-16
"""
from typing import Optional


# 160 Intersection of two linked List
# For question please go through below link:
# https://leetcode.com/problems/intersection-of-two-linked-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None and headB is None:
            return headA
        pointer_a = headA
        pointer_b = headB
        while pointer_a != pointer_b:
            if pointer_a is None:
                pointer_a = headB
            else:
                pointer_a = pointer_a.next

            if pointer_b is None:
                pointer_b = headA
            else:
                pointer_b = pointer_b.next
        return pointer_a


if __name__ == '__main__':
    listA = [4, 1, 8, 4, 5]
    listB = [5, 6, 1, 8, 4, 5]
    solution = Solution()
    result = solution.getIntersectionNode(listA, listB)
    print(result)
