# Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_lenght = float('inf')
        sum = 0
        l = 0

        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                min_lenght = min(min_lenght, r-l+1)
                sum -= nums[l]
                l += 1
            
        return min_lenght if min_lenght < float('inf') else 0
    
s = Solution()
print(s.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))