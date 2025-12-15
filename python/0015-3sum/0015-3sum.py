class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left_hash = {}
        right_hash = {}
        output = set()

        nums.sort()
        left_hash[nums[0]] = 1
        for i in range(1, len(nums)):
            if nums[i] not in right_hash:
                right_hash[nums[i]] = 0
            right_hash[nums[i]] += 1

        idx = 1
        while idx < len(nums) - 1:
            if nums[idx] in right_hash:
                right_hash[nums[idx]] -= 1
                if right_hash[nums[idx]] == 0:
                    del right_hash[nums[idx]]

            for n in left_hash.keys():
                target = -(n + nums[idx])
                if target in right_hash:
                    output.add((n, nums[idx], target))

            if nums[idx] in left_hash:
                left_hash[nums[idx]] += 1
            else:
                left_hash[nums[idx]] = 1

            idx += 1

        return list(output)
