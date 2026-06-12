#Group Anagrams

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_groups = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_groups[sorted_word].append(word)

        return list(anagram_groups.values())
    
    
# The Core Principle: Two words are anagrams if and only if their letters, when sorted, are exactly the identical. 
# For example, both "eat" and "tea" sort to "aet"

# Grouping: As you loop through the array, the code sorts each word, then appends the original word to the list associated with that sorted key.

# Efficiency: This gives a time complexity of O(N.KlogK), where N is the number of strings and K is the maximum length of a string.