class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        hashset = set()
        output = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    pivot = target - nums[i] - nums[j] - nums[k]
                    if pivot in hashset:
                        output.add(tuple(sorted([nums[i], nums[j], nums[k], pivot])))
            hashset.add(nums[i])
        
        return list(output)
        """
        output = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = len(nums) - 1

                while left < right:
                    pivot = target - nums[i] - nums[j]

                    if nums[left] + nums[right] < pivot:
                        left += 1
                    elif nums[left] + nums[right] > pivot:
                        right -= 1
                    else:
                        output.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                    
                        left += 1
                        right -= 1
        
        return output