"""
-- Created by Pravesh Budhathoki
-- Created on 2023-06-15
"""
from typing import List


# 27. Remove Element
# For better understanding od question please go through this link:
# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] != val:
                start += 1
                continue
            if nums[end] == val:
                end -= 1
                continue
            nums[start] = nums[end]
            start += 1
            end -= 1
        return start


if __name__ == '__main__':
    solution = Solution()
    _nums = [3, 2, 2, 3]
    _val = 3
    result = solution.removeElement(_nums, _val)
    print(result)
