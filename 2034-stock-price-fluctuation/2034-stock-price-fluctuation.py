class StockPrice:
    def __init__(self):
        self.stockMap = {}
        self.last_ts = 0
        self.minStock = []
        self.maxStock = []
        self.updated = set()

    def update(self, timestamp: int, price: int) -> None:
        self.stockMap[timestamp] = price

        heapq.heappush(self.minStock, (price, timestamp))
        heapq.heappush(self.maxStock, (-price, timestamp))

        if timestamp > self.last_ts:
            self.last_ts = timestamp

        return
    
    def current(self) -> int:
        return self.stockMap[self.last_ts]

    def maximum(self) -> int:
        max_stock, ts = self.maxStock[0]

        while self.maxStock and -max_stock != self.stockMap[ts]:
            heapq.heappop(self.maxStock)
            max_stock, ts = self.maxStock[0]
        
        return -max_stock
        
    def minimum(self) -> int:
        min_stock, ts = self.minStock[0]

        while self.minStock and min_stock != self.stockMap[ts]:
            heapq.heappop(self.minStock)
            min_stock, ts = self.minStock[0]
        
        return min_stock
# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()