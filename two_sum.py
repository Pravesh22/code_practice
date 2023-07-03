"""
-- Created by Pravesh Budhathoki
-- Created on 2023-05-30
"""
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

For more details: https://leetcode.com/problems/two-sum/
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_table:
                return [i, hash_table[diff]]
            else:
                hash_table[nums[i]] = i


if __name__ == '__main__':
    _target = 6
    _nums = [3, 3]
    solution = Solution()
    _result = solution.twoSum(nums=_nums, target=_target)
    print(_result)
