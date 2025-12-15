class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        l = len(matrix)

        for r in range(l):
            heapq.heappush(heap, (matrix[r][0], r, 0))

        count = 0

        while len(heap) > 0:
            cur_smallest, row, col = heapq.heappop(heap)

            count += 1
            if count == k:
                return cur_smallest

            if col < l - 1:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
