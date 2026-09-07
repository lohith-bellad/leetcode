class MRUQueue:

    def __init__(self, n: int):
        self.nums = [i for i in range(1, n + 1)]

    def fetch(self, k: int) -> int:
        elem = self.nums[k - 1]

        for i in range(k, len(self.nums)):
            self.nums[i - 1] = self.nums[i]
        
        self.nums[-1] = elem
        return elem
# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
        
# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)