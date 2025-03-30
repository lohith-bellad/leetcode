class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_find(nums: [int], start: int, end: int) -> int:
            ind = -1
            while start <= end:
                mid = start + (end - start) // 2

                if nums[mid] == target:
                    ind = mid
                    break
            
                if nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
        
            return ind
        
        output = []
        mid = binary_find(nums, 0, len(nums) - 1)

        if mid == -1:
            return [-1, -1]
        
        start = binary_find(nums, 0, mid - 1)
        if start == -1:
            output.append(mid)
        else:
            output.append(start)
        
        end = binary_find(nums, mid + 1, len(nums) - 1)
        if end == -1:
            output.append(mid)
        else:
            output.append(end)
        
        return output