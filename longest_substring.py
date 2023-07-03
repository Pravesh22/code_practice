"""
-- Created by Pravesh Budhathoki
-- Created on 2022-01-18 
"""

"""Given a string s, find the length of the longest substring without repeating characters."""

# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

def lengthOfLongestSubstring(s):
    i = j = longest_len = 0
    chars = dict()

    # empty string variable
    longest_str = ''
    while j < len(s):
        if s[j] not in chars:
            chars[s[j]] = j
            if len(chars) > longest_len:
                longest_str += s[j]
            j = j + 1
            longest_len = max(longest_len, len(chars))

        else:
            del chars[s[i]]
            i = i + 1
    return longest_len


if __name__ == '__main__':
    print(lengthOfLongestSubstring("bbbbb"))
    # print the longest substring with its length
    # print(f'The longest substring: {longest_str}, length: {longest_len}')