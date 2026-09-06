class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set()

        for num in nums:
            n = int(num, 2)
            seen.add(n)
        
        for i in range(len(nums) + 1):
            if i not in seen:
                return format(i, f"0{len(nums)}b")
        
        return ""