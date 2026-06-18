# Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        #convert the list to set - for fast lookup
        nums_set = set(nums)
        streak = 0

        for num in nums_set:
            #if num is the absolute start
            if (num - 1) not in nums_set:
                current_num = num
                curr_streak = 1

                while (current_num + 1) in nums_set:
                    current_num += 1
                    curr_streak += 1
                
                streak = max(streak, curr_streak)
        
        return streak