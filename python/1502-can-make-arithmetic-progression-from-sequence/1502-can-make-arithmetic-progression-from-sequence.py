class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]

        for num in range(2, len(arr)):
            if (arr[num] - arr[num - 1]) != diff:
                return False
        
        return True