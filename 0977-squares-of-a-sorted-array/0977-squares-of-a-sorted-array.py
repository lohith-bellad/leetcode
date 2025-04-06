class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda x: abs(x))
        output = []

        for num in nums:
            output.append(num**2)
        
        return output