class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        start_elem = min(nums)

        for i in range(len(nums)):
            if nums[i] == start_elem:
                break
        
        offset = i
        start = 0
        end = len(nums) - 1

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
        """
        if len(nums) <= 1:
            if len(nums) == 1 and nums[0] == target:
                return 0
            return -1
            
        start = 0
        end = len(nums) - 1
        offset = 0

        while start <= end:
            mid = start + (end - start) // 2

            if 0 < mid < len(nums) - 1:
                if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                    offset = mid
                    break

                if nums[mid] > nums[mid - 1]:
                    end = mid - 1

                if nums[mid] > nums[mid + 1]:
                    start = mid + 1
            else:
                if mid == 0 and nums[mid + 1] > nums[mid]:
                    offset = mid
                    break
                else:
                    start = mid + 1

                if mid == len(nums) - 1 and nums[mid] < nums[mid - 1]:
                    offset = mid
                    break
                else:
                    end = mid - 1

        if offset != mid:
            offset = start

        start = 0
        end = len(nums) - 1

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