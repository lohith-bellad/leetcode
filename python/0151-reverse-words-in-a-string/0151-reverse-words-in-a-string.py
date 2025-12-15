class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        output = ""

        i = len(words) - 1
        while i >= 0:
            if len(output) > 0:
                output += " "
            output += words[i]
            i -= 1

        return output
