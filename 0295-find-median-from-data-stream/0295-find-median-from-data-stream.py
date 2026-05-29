class MedianFinder:
    """
    def __init__(self):
        self.lo_arr = []
        self.hi_arr = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo_arr, -num)
        left_largest = -self.lo_arr[0]

        if self.hi_arr and left_largest > self.hi_arr[0]:
            n = heapq.heappop(self.lo_arr)
            heapq.heappush(self.hi_arr, -n)
        
        if len(self.lo_arr) > len(self.hi_arr) + 1:
            n = heapq.heappop(self.lo_arr)
            heapq.heappush(self.hi_arr, -n)
        
        elif len(self.hi_arr) > len(self.lo_arr) + 1:
            n = heapq.heappop(self.hi_arr)
            heapq.heappush(self.lo_arr, -n)
        
    def findMedian(self) -> float:
        if len(self.lo_arr) > len(self.hi_arr):
            return -self.lo_arr[0]
        elif len(self.hi_arr) > len(self.lo_arr):
            return self.hi_arr[0]
        
        return (self.hi_arr[0] - self.lo_arr[0]) / 2.0
    """
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        left_largest = heapq.heappop(self.maxHeap)

        heapq.heappush(self.minHeap, -left_largest)

        if len(self.minHeap) > len(self.maxHeap):
            right_smallest = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -right_smallest)
        
    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            num1 = self.minHeap[0]
            num2 = self.maxHeap[0]
            return (-num2 + num1) / 2.0
        
        val = self.maxHeap[0]
        return -val

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()