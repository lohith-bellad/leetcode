class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subarr_sum = 0
        count = 0

        for i in range(k):
            subarr_sum += arr[i]

        if (subarr_sum / k) >= threshold:
            count += 1

        start = 0
        end = k

        while end < len(arr):
            subarr_sum -= arr[start]
            subarr_sum += arr[end]
            if (subarr_sum / k) >= threshold:
                count += 1
            start += 1
            end += 1

        return count
