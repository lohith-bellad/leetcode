class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hashMap = defaultdict(list)
        m = len(mat)
        n = len(mat[0])

        for row in range(m):
            for col in range(n):
                key = row + col
                hashMap[key].append(mat[row][col])
        
        output = []
        for i in range(m + n - 1):
            if i % 2 == 0:
                hashMap[i].reverse()
            output += hashMap[i]
        
        return output