"""
680. Valid Palindrome II
Medium

Given a string s, return true if the s can be palindrome after deleting at most one character from it.


Example 1:
    Input: s = "aba"
    Output: true

Example 2:
    Input: s = "abca"
    Output: true
    Explanation: You could delete the character 'c'.

Example 3:
    Input: s = "abc"
    Output: false


Constraints:
    * 1 <= s.length <= 50000
    * s consists of lowercase English letters only

"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palin(start, end, skip):
            if start < end:
                if s[start] == s[end]:
                    return is_palin(start + 1, end - 1, skip)
                else:
                    if skip:
                        return is_palin(start + 1, end, False) or is_palin(start, end - 1, False)
                    else:
                        return False
            else:
                return True

        return is_palin(0, len(s) - 1, True)

        
