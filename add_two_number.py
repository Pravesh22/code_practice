"""
-- Created by Pravesh Budhathoki
-- Created on 2023-06-29
"""
from typing import Optional


# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = temp_node = ListNode()
        carry = 0
        while l1 or l2:
            if l1 is None:
                l1 = ListNode()
            if l2 is None:
                l2 = ListNode()
            remainder = (l1.val + l2.val + carry) % 10
            _sum = l1.val + l2.val + carry
            carry = _sum // 10
            temp_node.next = ListNode(remainder)
            temp_node = temp_node.next
            l1 = l1.next
            l2 = l2.next
        if carry == 1:
            temp_node.next = ListNode(carry)
        return dummy_node.next


if __name__ == '__main__':
    solution = Solution()
    _list1 = [0, 8, 8, 8, 8, 2, 9, 3, 1, 1]
    _list2 = [0, 9, 1, 5, 5, 5, 1, 1, 6]

    # creating ListNode from given list of integers
    l1_index = 0
    l2_index = 0
    dummy_node1 = temp_node1 = ListNode()
    dummy_node2 = temp_node2 = ListNode()

    while l1_index < len(_list1):
        temp_node1.next = ListNode(_list1[l1_index])
        temp_node1 = temp_node1.next
        l1_index += 1
    while l2_index < len(_list2):
        temp_node2.next = ListNode(_list2[l2_index])
        temp_node2 = temp_node2.next
        l2_index += 1
    _l1_node = dummy_node1.next
    _l2_node = dummy_node2.next
    result = solution.addTwoNumbers(_l1_node, _l2_node)
    print(result)
