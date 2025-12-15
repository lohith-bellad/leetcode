class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        heap = []
        output = []

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 0
            hash_map[num] += 1

        for key, v in hash_map.items():
            heapq.heappush(heap, (-v, key))

        while len(output) < k:
            (cnt, val) = heapq.heappop(heap)
            output.append(val)

        return output
