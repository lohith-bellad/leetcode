class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])

            if len(heap) > k:
                heapq.heappop(heap)

        max_elem = heapq.heappop(heap)

        return max_elem
