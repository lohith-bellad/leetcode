class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(si, pi):
            if pi >= len(p):
                return si >= len(s)

            if (si, pi) in cache:
                return cache[(si, pi)]

            match = si < len(s) and (s[si] == p[pi] or p[pi] == ".")

            if pi + 1 < len(p) and p[pi + 1] == "*":
                res = dfs(si, pi + 2) or (match and dfs(si + 1, pi))
            else:
                res = match and dfs(si + 1, pi + 1)

            cache[(si, pi)] = res
            return res

        cache = {}
        return dfs(0, 0)