class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        
        if len(nums) < k:
            return []

        output = []
        max_heap = []

        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))

        output.append(-max_heap[0][0])

        left = 0
        for right in range(k, len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))

            while len(max_heap) > k and max_heap[0][1] <= left:
                heapq.heappop(max_heap)

            output.append(-max_heap[0][0])
            left += 1            

        return output
        """
        max_heap = []
        output = []

        for i in range(len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))

            if len(max_heap) < k:
                continue

            found = False
            while not found:
                num, ind = heapq.heappop(max_heap)
                if ind > i - k:
                    found = True
                    output.append(-num)
                    heapq.heappush(max_heap, (num, ind))
            
        return output
