class Solution:
    def minCut(self, s: str) -> int:
        def set_palindrome(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                is_palindrome[i][j] = True
                i -= 1
                j += 1
            return

        def dfs(start):
            if start == len(s):
                return 0
            
            if start in cache:
                return cache[start]

            res = float('inf')
            for end in range(start, len(s)):
                if is_palindrome[start][end]:
                    res = min(res, dfs(end + 1) + 1)
            
            cache[start] = res
            return res

        n = len(s)
        is_palindrome = [[False for i in range(n)] for i in range(n)]
        cache = {}

        for start in range(n):
            set_palindrome(start, start)
            set_palindrome(start, start + 1)
        
        return dfs(0) - 1