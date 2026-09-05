class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(index):
            if index >= len(s):
                return 1

            if s[index] == "0":
                return 0

            if index in cache:
                return cache[index]
            
            r = dfs(index + 1)

            if index + 1 < len(s) and s[index] != "0" and int(s[index:index + 2]) <= 26:
                r += dfs(index + 2)

            cache[index] = r   
            return r

        cache = {}
        return dfs(0)