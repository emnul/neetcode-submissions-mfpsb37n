class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = collections.defaultdict(list) # tuple of letter counts -> list of words
        for s in strs:
            counts = [0] * 26
            for c in s:
                val = ord(c) - ord('a')
                counts[val] += 1
            hm[tuple(counts)].append(s)
        return list(hm.values())
        
