class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # in the previous solution we used the sorted string of each element as a key
        # for the grouping dict. Instead of sorting each string, we can use a list count the occurances
        # of each char in the string. Each index in the list will correspond to the ascii value of 
        # a char. ex "abc" -> [1, 1, 1, 0, ... 0]

        res = collections.defaultdict(list)
        for string in strs:
            bucket = [0] * 26 # 26 letters in alphabet
            for char in string:
                asciiVal = ord(char) - ord('a') # normalize char vals
                bucket[asciiVal] += 1
            res[tuple(bucket)].append(string)

        return list(res.values())
            