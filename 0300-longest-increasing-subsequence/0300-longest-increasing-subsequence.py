class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        output = []

        for num in nums:
            ind = bisect.bisect_left(output, num)
            if ind == len(output):
                output.append(num)
            else:
                output[ind] = num
        
        return len(output)
        """
        def find_ind(num):
            start = 0
            end = len(output)

            while start < end:
                mid = start + (end - start) // 2

                if output[mid] < num:
                    start = mid + 1
                else:
                    end = mid

            return start
        
        output = []

        for num in nums:
            ind = find_ind(num)

            if ind == len(output):
                output.append(num)
            else:
                output[ind] = num

        return len(output)