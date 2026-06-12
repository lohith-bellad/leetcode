class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        hashMap = {}

        for num in balls:
            hashMap[num] = hashMap.get(num, 0) + 1

        freqs = hashMap.values()

        for s in range(min(freqs) + 1, 0, -1):
            matched = True
            for f in freqs:
                if ceil(f / s) * (s - 1) > f:
                    matched = False
                    break
            if matched:
                output = 0
                for f in freqs:
                    output += ceil(f / s)
                return output
        
        return -1