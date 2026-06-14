#sort colors

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

#Dutch-National Flag Algorithm
# Set low and mid to the beginning index (0), and high to the last index of the array (len(nums) - 1).
#     low tracks the boundary where the next 0 should go.
#     mid scans through the elements.
#     high tracks the boundary where the next 2 should go

# How it works:
# Everything to the left of low is a 0.
# Everything to the right of high is a 2.
# Everything between low and mid - 1 is a 1.
# The elements from mid to high are unexamined.

# Step-by-Step Breakdown
# We initialize low = 0, mid = 0, and high = len(nums) - 1. We iterate while mid <= high:

# Case 1: nums[mid] == 0
# We swap nums[low] and nums[mid]. Because we know whatever was at low was a 1 (or mid and low were at the same spot), 
# we can safely move both pointers forward: low += 1, mid += 1.

# Case 2: nums[mid] == 1
# This is already in the correct middle zone. We just move the mid pointer forward: mid += 1.

# Case 3: nums[mid] == 2
# We swap nums[mid] and nums[high]. We then decrement high -= 1.

# Crucial Note: We do not move mid forward here. The element we just swapped from high into mid is unexamined—it could be a 0 or a 1, 
# so we need to evaluate it in the next iteration.