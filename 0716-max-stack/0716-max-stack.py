class MaxStack:

    def __init__(self):
        self.heap = []
        self.stack = []
        self.removed = set()
        self.ident = 0

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (-x, -self.ident))
        self.stack.append((x, self.ident))
        self.ident += 1
        return

    def pop(self) -> int:
        while len(self.stack) > 0 and self.stack[-1][1] in self.removed:
            self.stack.pop()
        elem, ident = self.stack.pop()
        self.removed.add(ident)
        return elem

    def top(self) -> int:
        while len(self.stack) > 0 and self.stack[-1][1] in self.removed:
            self.stack.pop()
        elem, ident = self.stack[-1]
        return elem

    def peekMax(self) -> int:
        while len(self.heap) > 0 and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        return -self.heap[0][0]

    def popMax(self) -> int:
        while len(self.heap) > 0 and -self.heap[0][1] in self.removed:
            heapq.heappop(self.heap)
        elem, ident = heapq.heappop(self.heap)
        self.removed.add(-ident)

        return -elem
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()