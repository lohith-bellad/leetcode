"""
516. Longest Palindromic Subsequence
Medium

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by
deleting some or no elements without changing the order of the remaining
elements.


Example 1:
    Input: s = "bbbab"
    Output: 4
    Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
    Input: s = "cbbd"
    Output: 2
    Explanation: One possible longest palindromic subsequence is "bb".


Constraints:
    * 1 <= s.length <= 1000
    * s consists only of lowercase English letters.

"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def dfs(start, end):
            if start > end:
                return 0

            if start == end:
                return 1

            if (start, end) in cache:
                return cache[(start, end)]

            if s[start] == s[end]:
                cache[(start, end)] = 2 + dfs(start + 1, end - 1)
            else:
                cache[(start, end)] = max(dfs(start + 1, end), dfs(start, end - 1))

            return cache[(start, end)]

        cache = {}
        return dfs(0, len(s) - 1)
