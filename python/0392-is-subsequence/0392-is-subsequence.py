class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind = 0

        for elem in s:
            while ind < len(t):
                if elem == t[ind]:
                    break
                ind += 1

            if ind >= len(t):
                return False
            else:
                ind += 1

        return True
