class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        output = end

        while start <= end:
            mid = start + (end - start)//2
            
            cur_sum = 0
            for p in piles:
                cur_sum += math.ceil(p/mid)

            if cur_sum <= h:
                output = min(output, mid)
                end = mid - 1
            else:
                start = mid + 1

        return output
