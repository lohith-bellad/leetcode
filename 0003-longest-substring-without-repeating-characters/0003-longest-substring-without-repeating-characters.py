class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        ctable = {}

        for right in range(len(s)):
            ctable[s[right]] = ctable.get(s[right], 0) + 1

            while left < right and ctable[s[right]] > 1:
                ctable[s[left]] -= 1
                if not ctable[s[left]]:
                    del ctable[s[left]]
                left += 1
            
            max_len = max(max_len, right - left + 1)

        return max_len
