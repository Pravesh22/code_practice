"""
-- Created by Pravesh Budhathoki
-- Created on 2023-06-26
"""


# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        count = 0
        sub_val = 1
        while x > 0:
            x -= sub_val
            if x < 0:
                break
            sub_val += 2
            count += 1
        return count

    def mySqrt2(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        for i in range(1, x + 1):
            if i * i > x:
                return i - 1
            continue

    def mySqrt3(self, x: int) -> int:
        # best solution1 using Newton-Raphson's Method
        res = 1
        for i in range(20):
            temp = res
            res = temp - (temp * temp - x) / (2 * temp)
        return int(res)

    def mySqrt4(self, x: int) -> int:
        if x <= 1:
            return x
        left, right = 2, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right -= 1
            else:
                left += 1
        return right

    def mySqrt5(self, x: int) -> int:
        # best solution so far using Newton Raphson iterative method
        val = 1
        for _ in range(20):
            val = (val + x / val) / 2
        return int(val)


if __name__ == "__main__":
    solution = Solution()
    _x = 2147395599
    result = solution.mySqrt5(_x)
    print(result)
