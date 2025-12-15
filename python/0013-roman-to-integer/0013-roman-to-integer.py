class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        ind = 0
        total = 0
        inp = []

        for c in s:
            inp.append(c)

        prev = "O"
        while len(inp) > 0:
            num = inp.pop()
            if prev == "O":
                total += roman_to_int[num]
            else:
                if roman_to_int[prev] > roman_to_int[num]:
                    total -= roman_to_int[num]
                else:
                    total += roman_to_int[num]
            prev = num

        return total
