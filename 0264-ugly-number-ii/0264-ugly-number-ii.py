class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = {2, 3, 5}
        minHeap = [1]
        seen = set([1])

        for _ in range(n):
            pivot = heapq.heappop(minHeap)

            for prime in primes:
                num = pivot * prime
                if num not in seen:
                    seen.add(num)
                    heapq.heappush(minHeap, num)
        
        return pivot