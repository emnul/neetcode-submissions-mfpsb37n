from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        maxF = 0
        l = 0
        hm = defaultdict(int) # cur char count in window

        for r in range(len(s)):
            hm[s[r]] += 1
            # update maxF when counts increase
            maxF = max(hm[s[r]], maxF)

            # check if we exhausted replacements in window
            if (r - l + 1) - maxF > k:
                # shift window left
                hm[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest

