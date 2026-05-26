# NOTES:
# defautldict is a good python struct to handle annoying missing key
# edge cases
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list) # mapping charCount to list of Anagrams

        # iter over list of strings
        for s in strs:
            # create buckets for each char
            count = [0] * 26 # a ... z

            # iter over each word
            for c in s:
                # normalize char values
                count[ord(c) - ord("a")] += 1
            # words with same char counts will map to same key          
            hm[tuple(count)].append(s)
        
        return list(hm.values())
        






