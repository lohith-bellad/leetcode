class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        count = 1
        elem = nums[0]

        for i in range(1, len(nums)):
            if elem == nums[i]:
                count += 1
            else:
                count -= 1

                if count == -1:
                    count = 1
                    elem = nums[i]

        return elem
        """
        major_elem = float('-inf')
        count = 1

        for num in nums:
            if num == major_elem:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                major_elem = num
                count = 1
        
        return major_elem