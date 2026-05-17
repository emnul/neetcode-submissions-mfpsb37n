from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Cannot be anagram is strings are different len
        if len(s) != len(t):
            return False
        
        sc = Counter(s)
        tc = Counter(t)

        return sc == tc
            
