class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
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
        """
        def check_count(num):
            hours_needed = 0

            for p in piles:
                hours_needed += math.ceil(p/num)

            return hours_needed <= h

        start = 1
        end = max(piles)

        while start < end:
            mid = start + (end - start) // 2

            if check_count(mid):
                end = mid
            else:
                start = mid + 1

        return end
