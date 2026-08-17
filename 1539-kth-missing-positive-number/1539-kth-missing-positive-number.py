class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 0
        end = len(arr)

        while start < end:
            mid = start + (end - start) // 2

            if arr[mid] - mid - 1 >= k:
                end = mid
            else:
                start = mid + 1
        
        return start + k