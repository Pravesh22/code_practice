"""
-- Created by Pravesh Budhathoki
-- Created on 2023-06-12
"""
from typing import List


# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges,
# and there is no integer x such that x is in one of the ranges but not in nums.
#
# Each range [a,b] in the list should be output as:
#     "a->b" if a != b
#     "a" if a == b
#
# Example 1:
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        _result = []
        i = 0
        len_nums = len(nums)
        while i < len_nums:
            current_val = nums[i]
            next_val = current_val
            while i + 1 < len_nums and nums[i + 1] == nums[i] + 1:
                i += 1
                next_val = nums[i]

            if current_val == next_val:
                _result.append(str(nums[i]))
            else:
                _result.append(f"{current_val}->{next_val}")
            i += 1
        return _result


if __name__ == '__main__':
    _nums = [0, 2, 3, 4, 6, 8, 9]
    solution = Solution()
    result = solution.summaryRanges(_nums)
    print(result)
