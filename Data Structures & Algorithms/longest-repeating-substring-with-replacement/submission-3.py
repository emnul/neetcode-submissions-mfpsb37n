from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l = 0
        longest = 0

        for r in range(len(s)): 
            counts[s[r]] += 1
            # window is valid so long as len - max(counts) <= k
            while r - l + 1 - max(counts.values()) > k:
                # window no longer valid so need to update counts and left ptr
                counts[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
