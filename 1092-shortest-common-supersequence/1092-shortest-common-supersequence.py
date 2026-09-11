class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        cache = {}

        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in cache:
                return cache[(i, j)]

            if str1[i] == str2[j]:
                res = 1 + dfs(i + 1, j + 1)
            else:
                res = 1 + min(dfs(i + 1, j), dfs(i, j + 1))

            cache[(i, j)] = res
            return res

        dfs(0, 0)                      # fill the memo

        out = []
        i = j = 0
        while i < m and j < n:         # walk forward, memo answers each choice
            if str1[i] == str2[j]:
                out.append(str1[i])
                i += 1
                j += 1
            elif dfs(i + 1, j) <= dfs(i, j + 1):
                out.append(str1[i])
                i += 1
            else:
                out.append(str2[j])
                j += 1

        out.append(str1[i:])           # tail drain, same trap as bottom-up
        out.append(str2[j:])
        return "".join(out)