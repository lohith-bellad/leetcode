class Solution:
    def customSortString(self, order: str, s: str) -> str:
        bitmap = [0 for i in range(26)]

        for c in s:
            bitmap[ord(c) - ord("a")] += 1

        output = ""
        for c in order:
            offset = ord(c) - ord("a")
            if bitmap[offset] > 0:
                output += c * bitmap[offset]
                bitmap[offset] = 0

        for i in range(26):
            if bitmap[i] > 0:
                output += chr(i + ord("a")) * bitmap[i]

        return output
