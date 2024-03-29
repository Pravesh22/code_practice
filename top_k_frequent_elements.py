"""
-- Created by Pravesh Budhathoki
-- Created on 2023-05-31
"""
from typing import List

"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
https://leetcode.com/problems/top-k-frequent-elements/
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for num in nums:
            if num in dictionary:
                count = dictionary.get(num) + 1
                dictionary[num] = count
            else:
                dictionary[num] = 1
        list_values = list(dictionary.values())
        result = []
        for i in range(k):
            frequency = list_values[i]
            number = list(dictionary.keys())[list_values.index(frequency)]
            result.append(number)
        return result


if __name__ == '__main__':
    solution = Solution()
    _nums = [1, 1, 2, 2, 2]
    _k = 2
    output = solution.topKFrequent(_nums, _k)
    print(output)
