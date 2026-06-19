# Subarray Sum Equals K

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_count = {0: 1}
        current_sum = 0
        result = 0

        for num in nums:
            current_sum += num
            #if there is a prefix sum that makes current_sum - k
            if (current_sum - k) in prefix_count:
                result += prefix_count[current_sum - k]
            #update prefix frequency
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1
        
        return result