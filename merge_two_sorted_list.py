"""
-- Created by Pravesh Budhathoki
-- Created on 2023-06-13
"""
from typing import Optional


# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        dummy = temp = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1.val
                list1 = list1.next
            else:
                temp.next = list2.val
                list2 = list2.next
            temp = temp.next
        if list1 is not None:
            temp.next = list1
        else:
            temp.next = list2
        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    list_node = ListNode()
    _list1 = [1, 2, 4]
    _list2 = [1, 3, 4]
    result = solution.mergeTwoLists(_list1, _list2)
