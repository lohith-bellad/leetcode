class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def binary_search(start: int, end: int) -> int:
            while start <= end:
                mid = start + (end - start) // 2

                if arr[mid] < x:
                    start = mid + 1
                else:
                    end = mid - 1

            return start

        right = binary_search(0, len(arr) - 1)
        left = right - 1

        while k > 0:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
            k -= 1

        return arr[left + 1 : right]
