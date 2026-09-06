class Solution:
    def countSubstrings(self, s: str) -> int:
        def find_palin(i, j):
            nonlocal count
            while i >= 0 and j < len(s) and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
            return
        
        count = 0

        for ind in range(len(s)):
            find_palin(ind, ind + 1)
            find_palin(ind, ind)

        return count