class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        size = len(s)
        cache = [[0 for i in range(size + 1)] for i in range(size + 1)]

        sr = s[::-1]
        for i in range(size):
            for j in range(size):
                if s[i] == sr[j]:
                    cache[i + 1][j + 1] = 1 + cache[i][j]
                else:
                    cache[i + 1][j + 1] = max(cache[i + 1][j], cache[i][j + 1])

        return cache[-1][-1] 