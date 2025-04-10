class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        size = len(s)
        cache = [[-1 for i in range(size)] for i in range(size)]

        def dfs(i: int, j: int) -> int:
            if i < 0 or j >= size:
                return 0
            
            if cache[i][j] != -1:
                return cache[i][j]

            if s[i] == s[j]:
                l = 1 if i == j else 2
                cache[i][j] = l + dfs(i - 1, j + 1)
            else:
                cache[i][j] = max(dfs(i - 1, j), dfs(i, j + 1))

            return cache[i][j]

        for i in range(size):
            dfs(i, i)
            dfs(i, i + 1)
        
        temp = []
        for r in range(size):
            temp.append(max(cache[r]))
        
        return max(temp)