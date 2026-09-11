class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def dfs(p, q):
            if p == len(str1) and q == len(str2):
                return 0
                
            if p == len(str1):
                return len(str2) - q
            if q == len(str2):
                return len(str1) - p
            
            if (p, q) in cache:
                return cache[(p, q)]
            
            if str1[p] == str2[q]:
                res = 1 + dfs(p + 1, q + 1)
            else:
                res = 1 + min(dfs(p, q + 1), dfs(p + 1, q))
            
            cache[(p, q)] = res
            return res

        output = []
        i = 0
        j = 0
        cache = {}

        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                output.append(str1[i])
                i += 1
                j += 1
            elif dfs(i + 1, j) <= dfs(i, j + 1):
                output.append(str1[i])
                i += 1
            else:
                output.append(str2[j])
                j += 1
        
        output.append(str1[i:])
        output.append(str2[j:])

        return "".join(output)