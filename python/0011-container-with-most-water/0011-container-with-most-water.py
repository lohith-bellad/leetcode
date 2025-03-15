class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0

        head = 0
        tail = len(height) - 1

        while head < tail:
            prod = min(height[head], height[tail])
            max_water = max(max_water, prod * (tail - head))

            if height[head] > height[tail]:
                tail -= 1
            else:
                head += 1
        
        return max_water