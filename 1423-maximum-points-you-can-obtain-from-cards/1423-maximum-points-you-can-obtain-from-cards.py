class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        if k >= len(cardPoints):
            return sum(cardPoints)

        cur_sum = 0
        max_sum = 0

        for i in range(k):
            cur_sum += cardPoints[i]

        max_sum = cur_sum

        i = k - 1
        j = len(cardPoints) - 1
        while i >= 0:
            cur_sum -= cardPoints[i]
            cur_sum += cardPoints[j]
            max_sum = max(max_sum, cur_sum)
            i -= 1
            j -= 1
        
        return max_sum
        """
        n = len(cardPoints)
        window = n - k
        cur_sum = 0
        min_sum = 0

        for i in range(window):
            cur_sum += cardPoints[i]
        
        min_sum = cur_sum
        right = window

        while right < n:
            cur_sum = cur_sum - cardPoints[right - window] + cardPoints[right]
            min_sum = min(cur_sum, min_sum)
            right += 1
        
        return sum(cardPoints) - min_sum


