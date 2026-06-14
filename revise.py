#we do revision here

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
        
            seen[num] = i
        
        return []
    
a = Solution()
print(a.twoSum([2, 8, 4, 7], 9))