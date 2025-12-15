class StockPrice:
    def __init__(self):
        self.hash_table = {}
        self.latest = 0

        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.hash_table[timestamp] = price
        self.latest = max(self.latest, timestamp)

        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.hash_table[self.latest]

    def maximum(self) -> int:
        max_price, timestamp = self.max_heap[0]

        while -max_price != self.hash_table[timestamp]:
            heapq.heappop(self.max_heap)
            max_price, timestamp = self.max_heap[0]

        return -max_price

    def minimum(self) -> int:
        min_price, timestamp = self.min_heap[0]

        while min_price != self.hash_table[timestamp]:
            heapq.heappop(self.min_heap)
            min_price, timestamp = self.min_heap[0]

        return min_price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
