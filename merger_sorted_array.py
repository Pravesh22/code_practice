"""
-- Created by Pravesh nums2udhathoki
-- Created on 2023-07-22
"""
from typing import List


# 88. Merge Sorted nums1rray
# For question please visit https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_pointer = m + n - 1
        while m > 0 and n > 0:
            if nums2[n - 1] > nums1[m - 1]:
                nums1[last_pointer] = nums2[n - 1]
                n -= 1
            elif nums2[n - 1] <= nums1[m - 1]:
                nums1[last_pointer] = nums1[m - 1]
                m -= 1
            last_pointer -= 1

        # filling nums1 with remaining num2 leftovers
        while n > 0:
            nums1[last_pointer] = nums2[n - 1]
            n -= 1
            last_pointer -= 1
        print(nums1)

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # second solution
        a, b, last_pointer = m - 1, n - 1, m + n - 1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[last_pointer] = nums1[a]
                a -= 1
            else:
                nums1[last_pointer] = nums2[b]
                b -= 1

            last_pointer -= 1


if __name__ == '__main__':
    _nums1 = [2, 0]
    _m = 1
    _nums2 = [1]
    _n = 1
    solution = Solution()
    solution.merge1(_nums1, _m, _nums2, _n)
