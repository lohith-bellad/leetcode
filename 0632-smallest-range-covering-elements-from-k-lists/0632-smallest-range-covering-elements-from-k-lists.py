class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minHeap = []
        curMax = float("-inf")
        smallRange = float("inf")
        output = [0, 0]

        for i in range(len(nums)):
            heapq.heappush(minHeap, (nums[i][0], i, 0))
            curMax = max(curMax, nums[i][0])
        
        while minHeap:
            curNode, list, ind = heapq.heappop(minHeap)

            curDiff = curMax - curNode
            if curDiff < smallRange:
                smallRange = curDiff
                output = [curNode, curMax]
            
            if ind + 1 >= len(nums[list]):
                break

            nextNode = nums[list][ind + 1]
            curMax = max(curMax, nextNode)
            heapq.heappush(minHeap, (nextNode, list, ind + 1))
            
        return output