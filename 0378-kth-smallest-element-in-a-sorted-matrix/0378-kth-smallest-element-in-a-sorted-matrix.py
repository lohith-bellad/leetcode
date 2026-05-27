class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        sortedNums = []

        for row in range(len(matrix)):
            heapq.heappush(minHeap, (matrix[row][0], row, 0))
        
        while k > 0:
            num, row, col = heapq.heappop(minHeap)
            k -= 1

            if col + 1 < len(matrix[0]):
                heapq.heappush(minHeap, (matrix[row][col + 1], row, col + 1))
        
        return num
        
        
        
