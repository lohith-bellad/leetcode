class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)

        for s, d, cost in flights:
            adj_list[s].append((d, cost))

        min_price = {}
        queue = deque()
        queue.append((src, 0, 0))

        while len(queue) > 0:
            city, price, hop_cnt = queue.popleft()

            if city in min_price and min_price[city] < price:
                continue
            else:
                min_price[city] = price

            if hop_cnt > k:
                continue

            for neighbor, hop_price in adj_list[city]:
                queue.append((neighbor, price + hop_price, hop_cnt + 1))
            
        if dst in min_price:
            return min_price[dst]
        else:
            return -1
