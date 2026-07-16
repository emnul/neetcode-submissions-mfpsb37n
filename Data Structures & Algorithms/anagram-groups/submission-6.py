from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list) # hm char counts -> str
        for s in strs:
            counts = [0] * 26 # each index represents char 'a' - 'z'
            for char in s:
                counts[ord(char) - ord('a')] += 1
            hm[tuple(counts)].append(s)
        return list(hm.values())