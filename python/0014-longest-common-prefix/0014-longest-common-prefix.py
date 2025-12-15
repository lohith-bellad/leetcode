class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        inp = sorted(strs, key=lambda x: len(x))

        output = inp[0]

        for i in range(1, len(inp)):
            ind = 0
            while ind < len(output) and inp[i][ind] == output[ind]:
                ind += 1
            output = output[:ind]

        return output
