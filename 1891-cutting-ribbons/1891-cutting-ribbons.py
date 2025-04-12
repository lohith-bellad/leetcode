class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def check(mid: int, count: int):
            c = 0

            for i in range(len(ribbons)):
                c += ribbons[i] // mid 
            
            print(mid)
            return c >= count

        start = 1
        end = max(ribbons)

        while start <= end:
            mid = start + (end - start) // 2

            if check(mid, k):
                start = mid + 1
            else:
                end = mid - 1
        
        return end