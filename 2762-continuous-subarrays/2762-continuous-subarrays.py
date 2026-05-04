class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        max_list = deque()
        min_list = deque()
        left = 0
        count = 0

        for right in range(len(nums)):
            while max_list and nums[max_list[-1]] <= nums[right]:
                max_list.pop()
            max_list.append(right)

            while min_list and nums[min_list[-1]] > nums[right]:
                min_list.pop()
            min_list.append(right)

            while nums[max_list[0]] - nums[min_list[0]] > 2:
                left += 1

                if max_list[0] < left:
                    max_list.popleft()
                if min_list[0] < left:
                    min_list.popleft()
            
            count += right - left + 1
        
        return count