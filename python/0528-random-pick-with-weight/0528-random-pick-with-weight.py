class Solution:
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


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
