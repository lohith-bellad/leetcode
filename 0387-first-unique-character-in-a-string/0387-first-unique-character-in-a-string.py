class Solution:
    def firstUniqChar(self, s: str) -> int:
        htable = {}

        for i in range(len(s)):
            htable[s[i]] = htable.get(s[i], 0) + 1
        
        for i in range(len(s)):
            if htable[s[i]] == 1:
                return i

        return -1