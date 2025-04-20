class Solution:
    def find_valley(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] > nums[-1]:
                start = mid + 1
            else:
                end = mid - 1
        return start

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 1:
            if len(nums) == 1 and nums[0] == target:
                return 0
            return -1

        start = 0
        end = len(nums) - 1
        offset = self.find_valley(nums)
        print(offset)
        while start <= end:
            mid = start + (end - start) // 2
            act_mid = (mid + offset) % len(nums)

            if nums[act_mid] == target:
                return act_mid

            if nums[act_mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1