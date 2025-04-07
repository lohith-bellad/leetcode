class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        out_str = []

        idx = 0
        while idx < len(nums):
            start = nums[idx]
            rang = [start]
            idx += 1
            while idx < len(nums) and start + 1 == nums[idx]:
                idx += 1
                start += 1
            rang.append(nums[idx - 1])
            output.append(rang)
        
        for each in output:
            if each[0] == each[1]:
                link = str(each[0])
            else:
                link = str(each[0]) + "->" + str(each[1])
            out_str.append(link)
        
        return out_str