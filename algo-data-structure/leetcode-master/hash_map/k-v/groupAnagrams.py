from typing import List


class Solution:
    """
    https://leetcode.com/problems/group-anagrams/

    key: the sorted word
    value: the list of words
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pool = {}
        
        for word in strs:
            key = "".join(sorted(word))
            pool[key] = pool.get(key, []) + [word]
        
        return pool.values()