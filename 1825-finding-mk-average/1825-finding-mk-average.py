class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.nums = deque()
        self.low = SortedList()
        self.mid = SortedList()
        self.high = SortedList()
        self.mid_sum = 0

    def _add(self, num: int):
        if self.low and num <= self.low[-1]:
            self.low.add(num)
        elif self.high and num >= self.high[0]:
            self.high.add(num)
        else:
            self.mid.add(num)
            self.mid_sum += num

    def _remove(self, num: int):
        if self.low and num <= self.low[-1]:
            self.low.remove(num)
        elif self.high and num >= self.high[0]:
            self.high.remove(num)
        else:
            self.mid.remove(num)
            self.mid_sum -= num

    def _rebalance(self):
        while len(self.low) > self.k:
            num = self.low.pop()
            self.mid.add(num)
            self.mid_sum += num

        while len(self.high) > self.k:
            num = self.high.pop(0)
            self.mid.add(num)
            self.mid_sum += num

        while len(self.low) < self.k and self.mid:
            num = self.mid.pop(0)
            self.low.add(num)
            self.mid_sum -= num

        while len(self.high) < self.k and self.mid:
            num = self.mid.pop()
            self.high.add(num)
            self.mid_sum -= num
    
    def addElement(self, num: int) -> None:
        self.nums.append(num)
        self._add(num)

        if len(self.nums) > self.m:
            n = self.nums.popleft()
            self._remove(n)

        self._rebalance()        

    def calculateMKAverage(self) -> int:
        if len(self.nums) < self.m:
            return -1

        return self.mid_sum // (self.m - (2 * self.k))


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()