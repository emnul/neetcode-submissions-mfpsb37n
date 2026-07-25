from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for s in strs:
            bucket = [0] * 26
            for c in s:
                ind = ord(c) - ord('a')
                bucket[ind] += 1
            hm[tuple(bucket)].append(s)
        
        return list(hm.values())