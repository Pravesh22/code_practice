"""
-- Created by Pravesh Budhathoki
-- Created on 2023-07-03
"""


# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
# Example 2:
# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result_str = ""
        result_len = 0
        for i in range(len(s)):
            # odd length
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result_len:
                    result_str = s[l: r + 1]
                    result_len = r - l + 1
                l -= 1
                r += 1

            # even length
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > result_len:
                    result_str = s[l: r + 1]
                    result_len = r - l + 1
                l -= 1
                r += 1
        return result_str


if __name__ == '__main__':
    solution = Solution()
    _s = "babbaaab"
    result = solution.longestPalindrome(_s)
    print(result)
