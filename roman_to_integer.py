"""
-- Created by Pravesh Budhathoki
-- Treeleaf Technologies Pvt. Ltd.
-- Created on 2022-01-08 
"""

"""To convert roman integer to number"""

def romanToInt(s):
    # Define the value of variable in dict format
    roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    n = len(s)
    num = roman_dict[s[n-1]]

    for i in range(n-2, -1, -1):
        if roman_dict[s[i]] >= roman_dict[s[i+1]]:
            num += roman_dict[s[i]]
        else:
            num -= roman_dict[s[i]]
    return num

if __name__ == '__main__':
    print(romanToInt("IX"))