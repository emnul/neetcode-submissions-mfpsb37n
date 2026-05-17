class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Cannot be anagram is strings are different len
        if len(s) != len(t):
            return False
        
        sd = {}
        td = {}
        for i in range(len(s)):
            # add char as key in dict for s
            if s[i] in sd:
                sd[s[i]] += 1
            else:
                sd[s[i]] = 1
            
            # add char as key in dict for t
            if t[i] in td:
                td[t[i]] += 1
            else:
                td[t[i]] = 1

        return sd == td
            
