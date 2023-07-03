"""
-- Created by Pravesh Budhathoki
-- Created on 2023-06-18
"""


# 28. Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#
# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        first_char = needle[0]
        len_needle = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == first_char:
                end_char_index = i + len_needle
                chars = haystack[i:end_char_index]
                if chars == needle:
                    return i
        return -1


if __name__ == '__main__':
    _haystack = "leetcode"
    _needle = "leeto"
    solution = Solution()
    result = solution.strStr(_haystack, _needle)
    print(result)
