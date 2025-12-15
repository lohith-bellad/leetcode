class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        """
        mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        inp = list(num)
        comp = list(num)
        comp.reverse()

        for a, b in zip(inp, comp):
            if a not in mapping or mapping[a] != b:
                return False

        return True
        """
        matches = {"0": "0", "6": "9", "1": "1", "8": "8", "9": "6"}

        start = 0
        end = len(num) - 1

        while start <= end:
            if num[end] in matches and num[start] == matches[num[end]]:
                start += 1
                end -= 1
            else:
                return False

        return True
