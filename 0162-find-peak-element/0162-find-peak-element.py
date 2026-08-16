class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        start = 0
        end = len(nums) - 1

        while start < end:
            mid = start + (end - start) // 2

            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid + 1
        
        return start
        
        if len(nums) == 1:
            return 0
            
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if 0 < mid < len(nums) - 1:
                if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                    return mid
                if nums[mid + 1] > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if mid == 0 and nums[mid] > nums[mid + 1]:
                    return mid
                elif mid == len(nums) - 1 and nums[mid] > nums[mid - 1]:
                    return mid

        return start
        """
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if ((mid - 1 < 0 or nums[mid - 1] < nums[mid]) and
                (mid + 1 > len(nums) - 1 or nums[mid + 1] < nums[mid])):
                return mid

            if mid > 0:
                if nums[mid - 1] > nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            elif mid < len(nums) - 1:
                if nums[mid + 1] > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1

        return start

