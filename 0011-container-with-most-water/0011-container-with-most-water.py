class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_quantity = 0

        while left < right:
            cur_quantity = (right - left) * min(height[left], height[right])
            max_quantity = max(max_quantity, cur_quantity)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_quantity