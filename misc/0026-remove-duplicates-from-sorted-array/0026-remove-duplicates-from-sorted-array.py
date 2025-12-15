class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        temp = [nums[0]]

        for i in range(1, len(nums)):
            if len(temp) == 0:
                temp.append(nums[i])
                continue

            if nums[i] != temp[-1]:
                temp.append(nums[i])

        for i in range(len(temp)):
            nums[i] = temp[i]

        return len(temp)
        """
        left = 0

        right = 1
        while right < len(nums):
            while right < len(nums) and nums[right] == nums[right - 1]:
                right += 1

            if right == len(nums):
                break

            left += 1
            nums[left] = nums[right]

            right += 1

        return left + 1
