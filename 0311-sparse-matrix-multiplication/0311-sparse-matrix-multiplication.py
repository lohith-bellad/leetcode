class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        """
        output = [[0 for i in range(len(mat2[0]))] for i in range(len(mat1))]

        for row in range(len(output)):
            non_zero = False
            for each in mat1[row]:
                if each != 0:
                    non_zero = True
                    break
            if not non_zero:
                continue
            for offset in range(len(output[0])):
                temp = 0
                for col in range(len(mat1[0])):
                    temp += mat1[row][col] * mat2[col][offset]
                output[row][offset] = temp
        
        return output
        """
        m = len(mat1)
        k = len(mat2)
        n = len(mat2[0])

        output = [[0 for i in range(n)] for i in range(m)]

        for row in range(m):
            all_zero = True
            for each in mat1[row]:
                if each != 0:
                    all_zero = False
                    break

            if all_zero:
                continue

            for offset in range(n):
                res = 0
                for col in range(k):
                    res += mat1[row][col] * mat2[col][offset]
                output[row][offset] = res

        return output