"""
-- Created by Pravesh Budhathoki
-- Created on 2023-06-15
"""
from typing import List


# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
            j += 1
        return i + 1


if __name__ == '__main__':
    solution = Solution()
    _nums = [1, 1, 2]
    result = solution.removeDuplicates(_nums)
    print(result)
