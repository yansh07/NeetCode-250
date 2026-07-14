# Trapping Rain Water

class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
            
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]
                
        return total_water
    

# Asli Logic Kya Hai?
# Kisi bhi ek building ke upar kitna paani rukega, ye sirf do cheezon par depend karta hai:

# 1. Us building ke left side me sabse unchi building kaun si hai.
# 2. Us building ke right side me sabse unchi building kaun si hai.

# Paani humesha dono side ki unchi buildings me se jo choti hogi (min), wahan tak bharega. 
# Aur usme se hum us building ki khud ki height minus kar denge.

# Formula:
# Water at index i = min(max_left, max_right) - height[i]


# Ye Code Kaam Kaise Kar Raha Hai? (Step-by-Step)
# 1.Pointers Initialization:Start and End.Humne left ko index 0 par aur right ko aakhri index par rakh diya. 
# Shuru me left_max aur right_max bhi inhi ki heights hain.

# 2.The Comparison:Deciding which side to move.Hum check karte hain ki left_max chota hai ya right_max. 
# Kyunki paani humesha kam unchi diwar tak hi ruk sakta hai, isliye hum humesha chote wale side ko aage badhate hain.

# 3.Updating Max & Adding Water:Pointer Movement.Agar hum left ko aage badha rahe hain, toh hum dekhte hain ki nayi building left_max se badi hai ya nahi. 
# Agar badi hai, toh ab ye hamari nayi boundary ban gayi (left_max update hoga). 
# Agar choti hai, toh iska matlab iske upar paani rukega! Kitna? left_max - current_height.

# 4.Meeting Point:Loop Ends.Ye process tab tak chalta hai jab tak left aur right pointers aapas me mil nahi jaate. Aakhri me total_water return ho jata hai.