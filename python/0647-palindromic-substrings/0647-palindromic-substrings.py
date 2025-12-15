class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        size = len(s)

        for i in range(size):
            left = i
            right = i

            while 0 <= left < size and 0 <= right < size and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            left = i
            right = i + 1

            while 0 <= left < size and 0 <= right < size and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count
