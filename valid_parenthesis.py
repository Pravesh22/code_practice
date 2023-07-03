"""
-- Created by Pravesh Budhathoki
-- Created on 2023-06-12
"""


# 20. Valid parenthesis
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for string in s:
            if string in ["(", "{", "["]:
                stack.append(string)
            elif string == ")" and len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            elif string == "}" and len(stack) != 0 and stack[-1] == "{":
                stack.pop()
            elif string == "]" and len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                return False
        return stack == []


if __name__ == '__main__':
    solution = Solution()
    _s = "["
    result = solution.isValid(_s)
    print(result)
