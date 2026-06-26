class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        single_num = 0

        for mask in range(32):
            cur_sum = 0

            for num in nums:
                cur_sum += num >> mask & 1

            bit = cur_sum % 3
            single_num |= (bit << mask)
        
        if single_num >= (1 << 31):
            single_num -= (1 << 32)

        return single_num
        """
        output = 0

        for shift in range(32):
            cur_sum = 0

            for num in nums:
                cur_sum += (num >> shift) & 1

            if cur_sum % 3:
                output |= (1 << shift)
        
        if output >= 2**31:
            output -= 2**32
            
        return output