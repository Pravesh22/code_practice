"""
-- Created by Pravesh Budhathoki
-- Created on 2022-01-08
"""

"""To find longest common prefix from given list of string, return "" if common prefix is not found"""


def longestCommonPrefix(strs):
    lcp = ""
    if strs is None or len(strs) == 0:
        return lcp

    minimum_length = len(strs[0])
    for i in range(1,len(strs)):
        minimum_length = min(minimum_length, len(strs[i]))

    for i in range(minimum_length):
        current_str = strs[0][i]

        for j in range(0,len(strs)):
            if current_str != strs[j][i]:
                return lcp
        lcp += current_str
    return lcp


if __name__ == '__main__':
    string = ["flower", "flow", "flight"]
    print(longestCommonPrefix(string))
