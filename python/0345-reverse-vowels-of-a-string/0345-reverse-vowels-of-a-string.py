class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        inp = list(s)

        start = 0
        end = len(s) - 1

        while start < end:
            if inp[start] in vowels and inp[end] in vowels:
                temp = inp[start]
                inp[start] = inp[end]
                inp[end] = temp
            elif inp[start] in vowels and inp[end] not in vowels:
                end -= 1
                continue
            elif inp[start] not in vowels and inp[end] in vowels:
                start += 1
                continue
            start += 1
            end -= 1

        return "".join(inp)
