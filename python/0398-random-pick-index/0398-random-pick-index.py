class Solution:
    def __init__(self, nums: List[int]):
        self.map = defaultdict(list)

        for i, val in enumerate(nums):
            self.map[val].append(i)

    def pick(self, target: int) -> int:
        idx = random.randint(0, len(self.map[target]) - 1)
        return self.map[target][idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
