class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
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
