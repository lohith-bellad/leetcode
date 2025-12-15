"""
409. Longest Palindrome
Easy

Given a string s which consists of lowercase or uppercase letters, return the length
of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


Example 1:
    Input: s = "abccccdd"
    Output: 7
    Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
    Input: s = "a"
    Output: 1
    Explanation: The longest palindrome that can be built is "a", whose length is 1.


Constraints:
    * 1 <= s.length <= 2000
    * s consists of lowercase and/or uppercase English letters only.

"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ctable = {}
        output = 0
        has_odd = False

        for c in s:
            ctable[c] = ctable.get(c, 0) + 1
        
        for _, value in ctable.items():
            if value % 2 == 0:
                output += value
            else:
                has_odd = True
                output += value - 1

        if has_odd:
            output += 1

        return output
