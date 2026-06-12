# Majority Element

class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        if not nums:
            return -1

        candidate = nums[0]
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1

        if nums.count(candidate) > len(nums) // 2:
            return candidate
        
        return -1

# the Boyer-Moore Voting Algorithm. 
# It is the optimal solution because it runs in O(n) time complexity and uses O(1) constant space complexity, outperforming hash map or sorting techniques
