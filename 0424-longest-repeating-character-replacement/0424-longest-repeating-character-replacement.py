class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        table = {}
        max_len = 0

        for right in range(len(s)):
            table[s[right]] = table.get(s[right], 0) + 1

            while right - left + 1 - max(table.values()) > k:
                table[s[left]] -= 1
                if not table[s[left]]:
                    del table[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
        
