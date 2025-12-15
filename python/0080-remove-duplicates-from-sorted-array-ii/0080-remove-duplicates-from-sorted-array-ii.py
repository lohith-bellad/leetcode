class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        pivot = 1
        count = 1
        start = 1

        while start < len(nums):
            if nums[start] != nums[start - 1]:
                count = 1
            else:
                count += 1
                if count > 2:
                    start += 1
                    continue
            nums[pivot] = nums[start]
            pivot += 1
            start += 1

        return pivot
