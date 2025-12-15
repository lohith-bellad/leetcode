class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0

        low = prices[0]
        for p in prices:
            if p < low:
                low = p
            output = max(output, p - low)
        return output
