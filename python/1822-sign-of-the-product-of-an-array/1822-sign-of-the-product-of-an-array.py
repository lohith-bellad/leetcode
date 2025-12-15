class Solution:
    @staticmethod
    def signFunc(val):
        if val < 0:
            return -1
        elif val > 0:
            return 1
        else:
            return 0

    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = 1

        for num in nums:
            product *= num

        return Solution.signFunc(product)
