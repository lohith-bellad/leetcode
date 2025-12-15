class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        mapping = {}

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if r + c in mapping:
                    mapping[r + c].append(mat[r][c])
                else:
                    mapping[r + c] = [mat[r][c]]

        temp = []
        row_max = len(mat)
        col_max = len(mat[0])
        for i in range(row_max + col_max - 1):
            temp.append(mapping[i])

        i = 0
        while i < len(temp):
            if i % 2 == 0:
                temp[i].reverse()
            i += 1

        output = []
        for t in temp:
            output += t

        return output
