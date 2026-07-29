class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        maxF = 0
        hm = collections.defaultdict(int)
        l = 0
        for r in range(len(s)):
            hm[s[r]] += 1
            maxF = max(maxF, hm[s[r]])

            # check if window is valid
            if (r - l + 1) - maxF > k:
                hm[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        return longest



