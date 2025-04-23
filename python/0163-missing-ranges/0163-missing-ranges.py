class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        """
        if lower == upper and len(nums) != 0:
            return []

        output = []
        for n in nums:
            if n > lower:
                output.append([lower, n - 1])
                lower = n + 1
            else:
                lower = n + 1

        if lower <= upper:
            output.append([lower, upper])

        return output
        """
        if lower == upper and len(nums) != 0:
            return []

        ranges = []

        for num in nums:
            if num > lower:
                ranges.append([lower, num - 1])
                lower = num + 1
            else:
                lower += 1

        if lower <= upper:
            ranges.append([lower, upper])

        return ranges

