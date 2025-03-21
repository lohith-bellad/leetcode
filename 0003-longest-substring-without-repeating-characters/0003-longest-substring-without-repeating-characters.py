class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        start = 0
        max_len = 0

        for i in range(len(s)):
            if s[i] not in table:
                table[s[i]] = i
                max_len = max(max_len, i - start + 1)
            else:
                while s[start] != s[i]:
                    del table[s[start]]
                    start += 1
                table[s[i]] = i
                start += 1
        
        return max_len
