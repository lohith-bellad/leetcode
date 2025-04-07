class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dup = set()
        total = 0

        l = len(grid)

        dup_num = 0
        for i in range(l):
            for j in range(l):
                if grid[i][j] in dup:
                    dup_num = grid[i][j]
                    break
                else:
                    dup.add(grid[i][j])
            if dup_num > 0:
                break
        
        output = [dup_num]
        for i in range(l):
            for j in range(l):
                total += grid[i][j]
        
        total -= output[0]
        s = l * l
        suma = (s * (s + 1)) // 2

        output.append(suma - total)

        return output