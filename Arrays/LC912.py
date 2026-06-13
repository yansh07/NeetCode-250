#Sort an array

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
        
        #divide the array into two halves
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])

        return self.merge(left_half, right_half)
    
    def merge(self, left: list[int], right:list[int]) -> list[int]:
        sorted_Array = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_Array.append(left[i])
                i += 1
            else:
                sorted_Array.append(right[j])
                j += 1
        sorted_Array.extend(left[i:])
        sorted_Array.extend(right[j:])

        return sorted_Array
    