class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each string in strs, sort, use sorted val as key in dict, return res
        
        sortedToGroup = collections.defaultdict(list)
        for string in strs:
            # strings are immutable in python
            sortedS = ''.join(sorted(string))
            sortedToGroup[sortedS].append(string)
        
        # {"aht": ["hat"], "act": ["act", "cat"], "opts": ["tops", "pots"]}
        # return list of values
        return list(sortedToGroup.values())