class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        row_max = len(boxGrid)
        col_max = len(boxGrid[0])

        output = [["" for i in range(row_max)] for i in range(col_max)]

        for i in range(col_max):
            for j in range(row_max):
                output[i][j] = boxGrid[j][i]

        for i in range(col_max):
            output[i].reverse()

        for i in range(row_max):
            bottom_most = col_max - 1
            for ind in range(col_max - 1, -1, -1):
                if output[ind][i] == "#":
                    output[ind][i] = "."
                    output[bottom_most][i] = "#"
                    bottom_most -= 1

                if output[ind][i] == "*":
                    bottom_most = ind - 1

        return output
