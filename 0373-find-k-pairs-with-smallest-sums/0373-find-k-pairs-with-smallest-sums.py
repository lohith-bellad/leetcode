class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        minHeap = []
        seen = set()
        output = []

        heapq.heappush(minHeap, (nums1[0] + nums2[1], 0, 0))
        seen.add((0, 0))

        while len(output) < k:
            _, i, j = heapq.heappop(minHeap)
            output.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1) and (i + 1, j) not in seen:
                heapq.heappush(minHeap, (nums1[i+1] + nums2[j], i + 1, j))
                seen.add((i + 1, j))
            
            if j + 1 < len(nums2) and (i, j + 1) not in seen:
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))
                seen.add((i, j + 1))
        
        return output