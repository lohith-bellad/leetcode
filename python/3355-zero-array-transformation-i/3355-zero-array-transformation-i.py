class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        temp = [0 for i in range(len(nums) + 1)]

        for r1, r2 in queries:
            temp[r1] += 1
            temp[r2 + 1] -= 1

        for i in range(1, len(temp)):
            temp[i] += temp[i - 1]

        print(temp)

        for i in range(len(nums)):
            if nums[i] > temp[i]:
                return False

        return True
