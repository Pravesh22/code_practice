"""
-- Created by Pravesh Budhathoki
-- Created on 2023-06-20
"""
from typing import List


# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        if target < nums[i]:
            return i
        while i < len(nums):
            if nums[i] == target:
                return i
            elif nums[i] > target > nums[i - 1]:
                return i
            i += 1
        return i


if __name__ == '__main__':
    solution = Solution()
    _nums = [1, 3, 5, 6]
    _target = 5
    result = solution.searchInsert(_nums, _target)
    print(result)
