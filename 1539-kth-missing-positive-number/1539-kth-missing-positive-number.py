class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []

        cnt = 1
        while len(missing) < k:
            if cnt not in arr:
                missing.append(cnt)
            cnt += 1

        return missing[-1]