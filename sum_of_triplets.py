"""
-- Created by Pravesh Budhathoki
-- Created on 2022-01-08 
"""

"""Given an integer array nums, return all the triplets [nums[i], nums[j], 
    nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0."""


def threeSum(nums):
    nums.sort()
    n = len(nums)
    result = []

    if n < 2:
        return []
    for i in range(n):
        head = i + 1
        end = n - 1
        if i > 0 and nums[i] == nums[i-1]:
            continue
        while head < end:
            if nums[i] + nums[head] + nums[end] == 0:
                result.append([nums[i], nums[head], nums[end]])
                head += 1
                while head < end and nums[head] == nums[head-1]:
                    head += 1
                end -= 1
                while head < end and nums[end] == nums[end+1]:
                    end -= 1
            elif nums[i]+nums[head]+nums[end] < 0:
                head += 1
                while head < end and nums[head] == nums[head-1]:
                    head += 1
            else:
                end -= 1
                while head < end and nums[end] == nums[end+1]:
                    end -= 1
    return result


if __name__ == '__main__':
    print(threeSum([-1,0,1,2,-1,-4]))

