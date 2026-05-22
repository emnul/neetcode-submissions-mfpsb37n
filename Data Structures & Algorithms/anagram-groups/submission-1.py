# NOTES:
# defautldict is a good python struct to handle annoying missing key
# edge cases
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list) # mapping charCount to list of Anagrams

        # iter over strs
        for s in strs:
            count = [0] * 26 # a ... z

            # iter over each word
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            hm[tuple(count)].append(s)
        
        return list(hm.values())
        






