class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def dfs(start, end):
            if end - start < 2:
                return 0

            if (start, end) in cache:
                return cache[(start, end)]
            res = 0

            for k in range(start + 1, end):
                cur_res = nums[start] * nums[k] * nums[end]
                res = max(res, dfs(start, k) + dfs(k, end) + cur_res)

            cache[(start, end)] = res
            return res

        nums = [1] + nums + [1]
        cache = {}
        return dfs(0, len(nums) - 1)