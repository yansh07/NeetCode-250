# Boats to save people

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        n = len(people)
        left, right = 0, n-1

        boats = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            
            right -= 1
            boats += 1
        return boats


s = Solution()
print(s.numRescueBoats([3, 2, 2, 1], 3))