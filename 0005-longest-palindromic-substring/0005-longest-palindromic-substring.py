class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find_max_length(i, j):
            nonlocal max_length
            nonlocal start
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > max_length:
                    max_length = j - i + 1
                    start = i
                i -= 1
                j += 1
            return
        
        max_length = 0
        start = -1

        for ind in range(len(s)):
            find_max_length(ind, ind + 1)
            find_max_length(ind, ind)

        return s[start:start + max_length]