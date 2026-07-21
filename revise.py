#we do revision here

class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        count_x = s.count(x)
        count_y = s.count(y)

        others = [char for char in s if char != x and char != y]
        return (y * count_y) + "".join(others) + (x * count_x)

s = Solution()
print(s.rearrangeString(s="aabc", x="a", y="c"))