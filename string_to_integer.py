"""
-- Created by Pravesh Budhathoki
-- Created on 2023-07-12
"""


# 8. String to Integer (atoi)
# For detailed question please visit https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi(self, s: str) -> int:
        list_str = list(s.strip())
        _result = "0"
        if len(list_str) == 0:
            return 0
        sign = -1 if list_str[0] == '-' else 1
        if list_str[0] in ['+', '-']:
            del list_str[0]

        i = 0
        while i < len(list_str) and list_str[i].isdigit():
            _result += list_str[i]
            i += 1
        _result = int(_result) * sign
        return max(pow(-2, 31), min(_result, pow(2, 31) - 1))


if __name__ == '__main__':
    _s = "21474836460"
    solution = Solution()
    result = solution.myAtoi(_s)
    print(result)
