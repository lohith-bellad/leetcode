class Solution:

    def __init__(self, w: List[int]):
        self.total = 0
        self.prefix_sum = []
        for n in w:
            self.total += n
            self.prefix_sum.append(self.total)

    def pickIndex(self) -> int:
        r_num = self.total * random.random()

        for i in range(len(self.prefix_sum)):
            if r_num <= self.prefix_sum[i]:
                return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()