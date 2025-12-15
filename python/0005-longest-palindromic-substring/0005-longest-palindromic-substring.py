class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = -1
        end = -1
        max_len = 0
        size = len(s)

        for i in range(size):
            left = i
            right = i

            while 0 <= left < size and 0 <= right < size and s[left] == s[right]:
                cur_len = right - left + 1
                if cur_len > max_len:
                    start = left
                    end = right
                    max_len = cur_len
                left -= 1
                right += 1

            left = i
            right = i + 1

            while 0 <= left < size and 0 <= right < size and s[left] == s[right]:
                cur_len = right - left + 1
                if cur_len > max_len:
                    start = left
                    end = right
                    max_len = cur_len
                left -= 1
                right += 1

        return s[start : end + 1]
