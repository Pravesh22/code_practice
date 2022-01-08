"""
-- Created by Pravesh Budhathoki
-- Created on 2022-01-08
"""

"""To convert roman integer to number"""

def romanToInt(s):
    # Define the value of variable in dict format
    ans = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    for a, b in zip(s, s[1:]):
      if roman[a] < roman[b]:
        ans -= roman[a]
      else:
        ans += roman[a]
    return ans + roman[s[-1]]

if __name__ == '__main__':
    print(romanToInt("MCMXCIV"))