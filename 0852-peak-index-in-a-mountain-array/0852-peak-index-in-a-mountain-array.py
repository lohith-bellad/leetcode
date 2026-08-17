class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        start = 0
        end = len(arr) - 1

        while start < end:
            mid = start + (end - start) // 2

            if arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid
        
        return start
        """
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if ((mid == 0 or arr[mid] > arr[mid - 1]) and 
                (mid == len(arr) - 1 or arr[mid] > arr[mid + 1])):
                return mid
            
            if arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1