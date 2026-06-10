class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        def getLetter(c, cnt):
            ind = ord(c) - ord('a')
            ind += cnt
            ind = ind % 26

            return chr(ord('a') + ind)
        
        shift = sum(shifts)
        output = ""

        for i in range(len(shifts)):
            if i > 0:
                shift -= shifts[i - 1]
            
            output += getLetter(s[i], shift)

        return output