from functools import reduce
from math import gcd

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = reduce(gcd, numsDivide)

        nums.sort()
        for i in range(len(nums)):
            if nums[i] > g:
                break
            
            if g % nums[i] == 0:
                return i
        
        return -1