class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        output = 0

        for i in range(k):
            output += max(happiness[i] - i, 0)
        
        return output