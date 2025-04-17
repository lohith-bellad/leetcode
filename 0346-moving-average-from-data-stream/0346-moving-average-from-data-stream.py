class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.nums = []

    def next(self, val: int) -> float:
        self.nums.append(val)

        if len(self.nums) > self.size:
            self.nums = self.nums[1:]

        return (1.0 * sum(self.nums))/len(self.nums)

"""   
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()

    def next(self, val: int) -> float:
        if len(self.queue) >= self.size:
            self.queue.popleft()
        self.queue.append(val)
        sums = sum(self.queue) * 1.0

        return sums / len(self.queue)

"""
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)