#Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        strs.sort()
        first = strs[0]
        last = strs[-1]

        prefix = ""
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            prefix += first[i]
        
        return prefix


# How it works: Instead of checking every single string, you only need to compare the first and the last string in the sorted list. 
# Any prefix shared by both the first and last element is guaranteed to be shared by all elements in between.
# Complexity: Time \(O(N \log N + M)\), Space O(1)