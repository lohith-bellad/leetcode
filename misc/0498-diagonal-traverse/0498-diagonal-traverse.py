class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        mat_map = defaultdict(list)
        row_max = len(mat)
        col_max = len(mat[0])

        for row in range(row_max):
            for col in range(col_max):
                mat_map[row + col].append(mat[row][col])
    
        indices = sorted(mat_map.keys())

        output = []
        for ind in indices:
            if ind % 2 == 0:
                mat_map[ind].reverse()
            output += mat_map[ind]
    
        return output
        
        """
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
        """