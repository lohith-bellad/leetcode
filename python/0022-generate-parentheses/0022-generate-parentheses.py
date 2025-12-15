class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def build(open: int, close: int, path: str, output: []):
            if open == 0 and close == 0:
                output.append(path)

            if open > 0:
                build(open - 1, close, path + "(", output)
            if close > open:
                build(open, close - 1, path + ")", output)
            return

        build(n, n, "", output)
        return output
