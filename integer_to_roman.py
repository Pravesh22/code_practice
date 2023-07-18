"""
-- Created by Pravesh Budhathoki
-- Created on 2023-07-18
"""


# 12. Integer to Roman
# For question please go to https://leetcode.com/problems/integer-to-roman/


class Solution:
    def intToRoman(self, num: int) -> str:
        # one solution
        map_int_to_roman = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD",
                            500: "D", 900: "CM", 1000: "M"}
        if num in map_int_to_roman:
            return map_int_to_roman[num]
        list_keys = list(map_int_to_roman.keys())
        _result = ""
        i = len(list_keys) - 1
        while 0 < num:
            if num < list_keys[i]:
                i -= 1
                continue
            else:
                num = num - list_keys[i]
                _result += map_int_to_roman[list_keys[i]]
        return _result

    def intToRoman1(self, num: int) -> str:
        # optimal solution than above (takes less time)
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        res = ""
        for i, v in enumerate(values):
            res += (num // v) * numerals[i]
            num %= v
        return res


if __name__ == '__main__':
    solution = Solution()
    _num = 995
    result = solution.intToRoman(_num)
    print(result)
