class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        mapping = {}
        output = float("-inf")

        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1

        for num in mapping.keys():
            outlier = total_sum - 2 * num

            if outlier in mapping:
                if outlier != num or mapping[outlier] > 1:
                    output = max(output, outlier)

        return output
