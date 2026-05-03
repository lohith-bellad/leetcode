class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(k):
            ctable = {}
            left = 0
            count = 0

            for right in range(len(nums)):
                ctable[nums[right]] = ctable.get(nums[right], 0) + 1

                while len(ctable) > k:
                    ctable[nums[left]] -= 1
                    if not ctable[nums[left]]:
                        del ctable[nums[left]]
                    left += 1
                
                count += right - left + 1
            
            return count
        
        return at_most(k) - at_most(k - 1)