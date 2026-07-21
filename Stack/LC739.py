# Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = []
        result = [0]* len(temperatures)

        for i, temp in enumerate(temperatures):
            while answer and temp > temperatures[answer[-1]]:
                idx = answer.pop()
                result[idx] = i - idx
            answer.append(i)
        return result