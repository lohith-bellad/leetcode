class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        output = []

        for x, y in points:
            distance = (x**2 + y**2) ** 0.5
            heapq.heappush(heap, (distance, x, y))

        for i in range(k):
            dist, x, y = heapq.heappop(heap)
            output.append([x, y])

        return output
