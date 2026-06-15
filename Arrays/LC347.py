# Top K Frequent Elements

# from collections import Counter

# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         count = Counter(nums)

#         # Create buckets where index represents the frequency
#         buckets = [[] for _ in range(len(nums) + 1)]

#         for num, freq in count.items():
#             buckets[freq].append(num)
        
#         result = []

#         # Traverse buckets backwards from highest frequency to lowest
#         for i in range(len(buckets) - 1, 0, -1):
#             for num in buckets[i]:
#                 result.append(num)
#                 if len(result) == k:
#                     return result
        

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)

        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))

            if len(heap)> k:
                heapq.heappop(heap)
    
        return [num for freq, num in heap]