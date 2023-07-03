"""
-- Created by Pravesh Budhathoki
-- Created on 2023-06-12
"""


# Given an integer x, return true if x is a palindrome, and false otherwise.
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        div = 1
        while x >= div * 10:
            div *= 10

        while x:
            right = x % 10
            left = x // div

            if left != right:
                return False
            x = (x % div) // 10
            div = div / 100
        return True


if __name__ == '__main__':
    _x = 121
    solution = Solution()
    result = solution.isPalindrome(_x)
    print(result)
