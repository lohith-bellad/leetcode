class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        farthest = [0 for i in range(n + 1)]

        for i in range(n + 1):
            left = max(0, i - ranges[i])
            farthest[left] = max(farthest[left], i + ranges[i])
        
        taps = 0
        curEnd = 0
        nextEnd = 0
        
        for i in range(n + 1):
            if i > nextEnd:
                return -1
            
            if i > curEnd:
                taps += 1
                curEnd = nextEnd
            
            nextEnd = max(nextEnd, farthest[i])
        
        return taps