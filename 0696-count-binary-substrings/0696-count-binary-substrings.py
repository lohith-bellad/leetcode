class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        output = 0
        prev = 0
        cur = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                output += min(cur, prev)
                prev = cur
                cur = 1
        
        output += min(cur, prev)
        return output


