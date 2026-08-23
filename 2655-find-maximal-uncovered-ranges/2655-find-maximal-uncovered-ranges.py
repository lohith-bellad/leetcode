class Solution:
    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
        ranges.sort()
        last_covered = -1
        output = []

        for start, end in ranges:
            if last_covered + 1 < start:
                output.append([last_covered + 1, start - 1])

            last_covered = max(end, last_covered)
        
        if last_covered + 1 < n:
            output.append([last_covered + 1, n - 1])
        return output