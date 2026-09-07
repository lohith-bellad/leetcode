class MovingAverage:
    def __init__(self, size):
        self.nums = deque()
        self.size = size
        self.sum = 0

    def next(self, val):
        self.nums.append(val)
        self.sum += val

        if len(self.nums) < self.size:
            return self.sum * 1.0 / len(self.nums)

        if len(self.nums) > self.size:
            self.sum -= self.nums.popleft()

        return self.sum * 1.0 / self.size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)