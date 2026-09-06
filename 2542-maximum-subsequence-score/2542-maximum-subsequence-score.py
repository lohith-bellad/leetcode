class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap = []
        curSum = 0
        output = 0
        pairs = sorted(list(zip(nums1, nums2)), key = lambda a:a[1], reverse = True)
        print(pairs)
        
        for (p, q) in pairs:
            heappush(heap, p)
            curSum += p

            if len(heap) > k:
                curSum -= heappop(heap)
            if len(heap) == k:
                output = max(output, curSum * q)

        return output