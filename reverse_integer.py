"""
-- Created by Pravesh Budhathoki
-- Created on 2023-07-10
"""


# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
# signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1:
# Input: x = 123
# Output: 321
#
# Example 2:
# Input: x = -123
# Output: -321
#
# Example 3:
# Input: x = 120
# Output: 21

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = 1
        if x < 0:
            sign = -1
            x *= sign
        while x:
            rem = x % 10
            x = x // 10
            result = result * 10 + rem
        # resultant integer value must be less than 2^31 and greater than 2^-31
        if result > pow(2, 31) or result < pow(2, -31):
            return 0
        return result * sign


if __name__ == '__main__':
    solution = Solution()
    _x = 1534236469
    result = solution.reverse(_x)
    print(result)
