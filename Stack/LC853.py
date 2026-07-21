# Car Fleet

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, vel in cars:
            time_to_target = (target - pos) / vel
            
            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)
            
        return len(stack)