class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def dfs(i, j):
            if i > j:
                return 0
            
            if i == j:
                return 1
            
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == s[j]:
                res =  dfs(i + 1, j - 1) + 2
            else:
                res = max(dfs(i + 1, j), dfs(i, j - 1))

            cache[(i, j)] = res
            return res

        cache = {}
        return dfs(0, len(s) - 1)