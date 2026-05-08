class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        pivot = -1

        for idx in range(len(nums) - 2, -1 , -1):
            if nums[idx] < nums[idx + 1]:
                pivot = idx
                break

        if pivot == -1:
            nums.reverse()
            return

        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] > nums[pivot]:
                nums[idx], nums[pivot] = nums[pivot], nums[idx]
                break

        nums[pivot + 1:] = reversed(nums[pivot + 1:])
        return
        """
        pivot = -1

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i - 1
                break
        
        if pivot == -1:
            nums.reverse()
            return
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        nums[pivot + 1:len(nums)] = nums[pivot + 1:len(nums)][::-1]

        return