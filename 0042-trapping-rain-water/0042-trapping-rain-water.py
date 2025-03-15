class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0 for i in range(len(height))]
        right = [0 for i in range(len(height))]
        output = 0

        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(left[i - 1], height[i])
        
        right[-1] = height[-1]
        for i in range(len(height) -2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        for i in range(len(height)):
            output += min(left[i], right[i]) - height[i]

        return output