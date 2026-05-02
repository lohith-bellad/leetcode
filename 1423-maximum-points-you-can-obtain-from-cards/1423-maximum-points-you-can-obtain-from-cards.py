class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window = n - k
        cur_sum = 0
        min_sum = 0

        for i in range(window):
            cur_sum += cardPoints[i]
        
        min_sum = cur_sum
        right = window

        for right in range(window, n):
            cur_sum = cur_sum - cardPoints[right - window] + cardPoints[right]
            min_sum = min(cur_sum, min_sum)
        
        return sum(cardPoints) - min_sum


