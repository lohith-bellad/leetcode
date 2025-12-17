"""
5. Longest Palindromic Substring
Medium

Given a string s, return the longest palindromic substring in s.


Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

Example 2:
    Input: s = "cbbd"
    Output: "bb"


Constraints:
    * 1 <= s.length <= 1000
    * s consist of only digits and English letters.

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        start_idx = 0
        max_len = 0
        
        for start in range(len(s)):
            i = start
            j = start

            while i >= 0 and j < len(s) and s[i] == s[j]:
                cur_len = j - i + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start_idx = i
                i += 1
                j -= 1

            i = start
            j = start + 1

            while i >= 0 and j < len(s) and s[i] == s[j]:
                cur_len = j - i + 1
                if cur_len > max_len:
                    max_len = cur_len
                    start_idx = i
                i += 1
                j -= 1

        return s[start_idx: start_idx + max_len]
