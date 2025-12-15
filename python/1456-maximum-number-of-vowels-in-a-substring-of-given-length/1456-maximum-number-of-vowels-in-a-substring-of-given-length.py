class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        max_cnt = 0
        cnt = 0

        for i in range(k):
            if s[i] in vowels:
                cnt += 1

        max_cnt = cnt
        start = 0

        while start < len(s) - k:
            if s[start] in vowels:
                cnt -= 1

            if s[start + k] in vowels:
                cnt += 1

            start += 1

            max_cnt = max(max_cnt, cnt)

        return max_cnt
