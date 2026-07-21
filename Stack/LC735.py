# Asteroid Collision

class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                diff = asteroid + stack[-1]

                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroid)
            
        return stack