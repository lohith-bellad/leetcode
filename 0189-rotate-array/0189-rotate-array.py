class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        

        size = len(nums)
        k = k % size

        count = 0
        start = 0

        while count < size:
            cur_idx = start
            prev_num = nums[cur_idx]

            while True:
                next_idx = (cur_idx + k) % size
                nums[next_idx], prev_num = prev_num, nums[next_idx]
                cur_idx = next_idx
                count += 1

                if start == cur_idx:
                    break
            
            start += 1
        
        return
        """
        k = k % len(nums)

        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]

        return
