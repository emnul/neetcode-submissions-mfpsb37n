from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            counts = [0] * 26
            for char in s:
                i = ord(char) - ord('a')
                counts[i] += 1
            t = tuple(counts)
            if t not in hm:
                hm[t] = [s]
            else:
                hm[t].append(s)
        
        return list(hm.values())