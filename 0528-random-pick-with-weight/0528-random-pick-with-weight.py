class Solution:
    """
    def __init__(self, w: List[int]):
        self.total = 0
        self.prefix_sum = []
        for n in w:
            self.total += n
            self.prefix_sum.append(self.total)

    def pickIndex(self) -> int:
        r_num = self.total * random.random()

        start = 0
        end = len(self.prefix_sum)

        while start < end:
            mid = start + (end - start) // 2

            if r_num > self.prefix_sum[mid]:
                start = mid + 1
            else:
                end = mid
        return start
    """
    def __init__(self, w: List[int]):
        self.prefixSum = []

        for num in w:
            if not self.prefixSum:
                self.prefixSum.append(num)
            else:
                self.prefixSum.append(self.prefixSum[-1] + num)

    def pickIndex(self) -> int:
        randInd = self.prefixSum[-1] * random.random()

        start = 0
        end = len(self.prefixSum) - 1

        while start < end:
            mid = start + (end - start) // 2

            if self.prefixSum[mid] == randInd:
                return mid

            if self.prefixSum[mid] > randInd:
                end = mid
            else:
                start = mid + 1
        
        return start
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()