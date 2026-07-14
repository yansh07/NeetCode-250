# Container with most water

class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        max_water = 0
        left, right = 0, n-1

        while left < right:
            current_water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, current_water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water