#Remove Element

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


# Logic: Maintain a pointer k to track the position for the next valid element. 
# Iterate through the array; if an element is not val, move it to the k-th position and increment k.