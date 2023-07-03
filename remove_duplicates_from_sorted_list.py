"""
-- Created by Pravesh Budhathoki
-- Created on 2023-06-14
"""
from typing import Optional


# 83. Remove Duplicates from Sorted List

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well
# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]
#
# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Constraints:
#     The number of nodes in the list is in the range [0, 300].
#     -100 <= Node.val <= 100
#     The list is guaranteed to be sorted in ascending order.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        dummy = head
        while dummy.next:
            if dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        return head


if __name__ == '__main__':
    solution = Solution()
    _list = [1, 1, 2]
    result = solution.deleteDuplicates(_list)
    print(result)
