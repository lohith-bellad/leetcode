class Solution:
    def rob(self, nums: List[int]) -> int:
        def find(nums: [], ind: int, memo: []) -> int:
            if ind == len(nums) - 1 or ind == len(nums) - 2:
                return nums[ind]

            if memo[ind] != -1:
                return memo[ind]

            max_money = 0
            i = ind + 2
            while i < len(nums):
                money = find(nums, i, memo)
                max_money = max(max_money, money)
                i += 1

            memo[ind] = max_money + nums[ind]

            return memo[ind]

        def rob_path(nums: List[int], memo: []) -> int:
            prev_sum = 0
            cur_sum = 0

            return max(find(nums, 0, memo), find(nums, 1, memo))

        memo1 = [-1 for i in range(len(nums) - 1)]
        memo2 = [-1 for i in range(len(nums) - 1)]
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(rob_path(nums[:-1], memo1), rob_path(nums[1:], memo2))
