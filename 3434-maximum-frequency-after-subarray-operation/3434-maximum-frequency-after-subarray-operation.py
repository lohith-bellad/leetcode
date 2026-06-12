class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        kCount = nums.count(k)
        output = 0

        for pivot in range(1, 51):
            if pivot == k:
                continue

            count = 0
            for num in nums:
                if num == pivot:
                    count += 1
                if num == k:
                    count -= 1
                count = max(count , 0)
                output = max(output, count)
        
        return output + kCount