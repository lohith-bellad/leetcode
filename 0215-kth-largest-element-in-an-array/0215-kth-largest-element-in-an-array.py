class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, -nums[i])

        i = 0
        while i < k:
            max_elem = -heapq.heappop(heap)
            i += 1
        
        return max_elem
        """
        heap = []
        heapq.heapify(heap)

        count_map = {}

        for num in nums:
            if num not in count_map:
                count_map[num] = 1
                heapq.heappush(heap, -num)
            else:
                count_map[num] += 1
    
        cnt = 0

        while cnt < k:
            n = heapq.heappop(heap)
            cnt += count_map[-n]
    
        return -n
