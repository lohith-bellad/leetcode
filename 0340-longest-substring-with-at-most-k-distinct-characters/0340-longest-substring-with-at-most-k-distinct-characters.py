class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
            ctable = {}
            left = 0
            max_len = float("-inf")

            for right in range(len(s)):
                ctable[s[right]] = ctable.get(s[right], 0) + 1

                while len(ctable) > k:
                    ctable[s[left]] -= 1
                    if not ctable[s[left]]:
                        del ctable[s[left]]
                    left += 1
                
                max_len = max(max_len, right - left + 1)
            
            return max_len