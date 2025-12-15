class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        for c1, c2 in zip(word1, word2):
            output += c1 + c2

        output += word1[len(output) // 2 :] + word2[len(output) // 2 :]

        return output
