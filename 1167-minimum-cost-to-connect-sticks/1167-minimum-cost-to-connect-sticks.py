class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        minHeap = []
        output = 0

        for stick in sticks:
            heapq.heappush(minHeap, stick)

        while len(minHeap) > 1:
            s1 = heapq.heappop(minHeap)
            s2 = heapq.heappop(minHeap)

            cur_sum = s1 + s2
            output += cur_sum

            heapq.heappush(minHeap, cur_sum)
        
        return output