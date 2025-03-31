class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_find(nums: [int], start: int, end: int, is_first: bool) -> int:
            while start <= end:
                mid = start + (end - start) // 2

                if nums[mid] == target:
                    if is_first:
                        if mid == start or nums[mid - 1] < target:
                            return mid
                        end = mid - 1
                    else:
                        if mid == end or nums[mid + 1] > target:
                            return mid
                        start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
        
            return -1
        
        start = binary_find(nums, 0, len(nums) - 1, True)
        end = binary_find(nums, 0, len(nums) - 1, False)
        
        return [start, end]