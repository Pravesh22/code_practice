"""
-- Created by Pravesh Budhathoki
-- Created on 2023-05-30
"""
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

For more details: https://leetcode.com/problems/group-anagrams/description/
"""
from typing import List


class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        alpha_char = "abcdefghijklmnopqrstuvwxyz"

        if len(strs) == 1:
            if len(strs[0]) == "":
                return [[""]]
            elif strs[0] in alpha_char:
                return [[strs[0]]]
        dictionary = {}
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str not in dictionary:
                dictionary[sorted_str] = [strs[i]]
            else:
                dictionary[sorted_str].append(strs[i])
        return list(dictionary.values())


if __name__ == '__main__':
    string_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    output = solution.groupAnagrams(strs=string_list)
    print(output)
