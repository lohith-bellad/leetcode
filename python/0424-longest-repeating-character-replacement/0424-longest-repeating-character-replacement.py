class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = {}
        max_size = 1
        left = 0

        for right in range(len(s)):
            if s[right] in table:
                table[s[right]] += 1
            else:
                table[s[right]] = 1

            while (right - left + 1) - max(table.values()) > k:
                table[s[left]] -= 1
                left += 1

            max_size = max(max_size, right - left + 1)

        return max_size
