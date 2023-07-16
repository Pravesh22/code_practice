"""
-- Created by Pravesh Budhathoki
-- Created on 2023-07-16
"""
from typing import List


# 11. Container With Most Water
# For question please visit following link https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea1(self, height: List[int]) -> int:
        # brute force solution. O(n^2) Time complexity
        max_area = 0
        for i in range(len(height) - 1):
            for j in range(i, len(height)):
                h = min(height[i], height[j])
                w = j - i
                area = h * w
                if max_area < area:
                    max_area = area
        return max_area

    def maxArea(self, height: List[int]) -> int:
        # optimal solution is this. Only scans arrays one time.Time complexity O(n)
        max_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            w = abs(right - left)
            h = min(height[left], height[right])
            area = h * w
            # moving the pointer which has low line value
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if max_area < area:
                max_area = area
        return max_area


if __name__ == '__main__':
    solution = Solution()
    _height = [1, 8, 7, 2, 5, 4, 8, 3, 5]
    # _height = [1, 1]
    result = solution.maxArea(_height)
    print(result)
