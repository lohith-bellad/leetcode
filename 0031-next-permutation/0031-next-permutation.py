class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i = i - 1

        if i >= 0:
            ind = len(nums) - 1

            while ind >= 0 and nums[ind] <= nums[i]:
                ind = ind - 1

            nums[ind], nums[i] = nums[i], nums[ind]

        left = i + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return
        """
        pivot = -1

        for i in range(len(nums) - 2, -1 , -1):
            cur_num = nums[i]
            next_num = nums[i+1]

            if cur_num < next_num:
                pivot = i
                break

        if pivot == -1:
            nums.reverse()
            return

        i = len(nums) - 1
        while i > pivot and nums[i] <= nums[pivot]:
            i -= 1

        nums[pivot], nums[i] = nums[i], nums[pivot]
        nums[pivot + 1:] = reversed(nums[pivot + 1:])

        return