from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list) # mapping from counts to string list
        for s in strs:
            counts = [0] * 26
            for char in s:
                i = ord(char) - ord('a')
                counts[i] += 1
            hm[tuple(counts)].append(s)
        
        return list(hm.values())