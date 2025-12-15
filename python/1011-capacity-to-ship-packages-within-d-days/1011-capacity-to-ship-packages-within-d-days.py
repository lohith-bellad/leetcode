class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lower = -1
        upper = 0

        for weight in weights:
            lower = max(lower, weight)
            upper += weight

        while lower < upper:
            capacity = lower + (upper - lower) // 2
            cnt_days = 1
            cur_size = 0

            idx = 0
            while idx < len(weights):
                if cur_size + weights[idx] > capacity:
                    cnt_days += 1
                    cur_size = 0
                else:
                    cur_size += weights[idx]
                    idx += 1

            if cnt_days > days:
                lower = capacity + 1
            else:
                upper = capacity

        return lower
