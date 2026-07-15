from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            counts = tuple(sorted(Counter(s).items()))
            if counts not in hm:
                hm[counts] = [s]
            else:
                hm[counts].append(s)
            print(s)
            print(counts)
        
        return list(hm.values())