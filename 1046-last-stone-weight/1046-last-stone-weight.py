class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        while len(maxHeap) > 1:
            max1 = heapq.heappop(maxHeap)
            max2 = heapq.heappop(maxHeap)
            max1 = -max1
            max2 = -max2

            if max2 < max1:
                new_max = max1 - max2
                heapq.heappush(maxHeap, -new_max)
        
        if not maxHeap:
            return 0
            
        return -maxHeap[0]
